from puresasl.client import SASLClient


class Client(object):

    def __init__(self):
        self.lasterror = ''
        self.attributes = {}
        self.sasl = None

    # Set attributes to be used in authenticating the session.  All attributes should be set
    # before init() is called.
    #
    # @param key Name of attribute being set
    # @param value Value of attribute being set
    # @return true iff success.  If false is returned, call getError() for error details.
    #
    # Available attribute keys:
    #
    #    service      - Name of the service being accessed
    #    username     - User identity for authentication
    #    authname     - User identity for authorization (if different from username)
    #    password     - Password associated with username
    #    host         - Fully qualified domain name of the server host
    #    maxbufsize   - Maximum receive buffer size for the security layer
    #    minssf       - Minimum acceptable security strength factor (integer)
    #    maxssf       - Maximum acceptable security strength factor (integer)
    #    externalssf  - Security strength factor supplied by external mechanism (i.e. SSL/TLS)
    #    externaluser - Authentication ID (of client) as established by external mechanism

    def setAttr(self, key, value):
        self.attributes[key] = value

    # Initialize the client object.  This should be called after all of the properties have been set.
    #
    # @return true iff success.  If false is returned, call getError() for error details.

    def getAttr(self, key):
        return self.attributes[key]

    def init(self):
        return True

    # Start the SASL exchange with the server.
    #
    # @param mechList List of mechanisms provided by the server
    # @param chosen The mechanism chosen by the client
    # @param initialResponse Initial block of data to send to the server
    #
    # @return true iff success.  If false is returned, call getError() for error details.

    def start(self, chosen):
        self.sasl = SASLClient(self.attributes['host'], mechanism=chosen, callback=self.getAttr)
        # ret, (bytes)chosen_mech, (bytes)initial_response = self.sasl.start(self.mechanism)
        return True, chosen.encode(), self.sasl.process()

    # Step the SASL handshake.
    #
    # @param challenge The challenge supplied by the server
    # @param response (output) The response to be sent back to the server
    #
    # @return true iff success.  If false is returned, call getError() for error details.
            
    def step(self, challenge):
        return True, self.sasl.process(challenge)

    # Encode data for secure transmission to the server.
    #
    # @param clearText Clear text data to be encrypted
    # @param cipherText (output) Encrypted data to be transmitted
    #
    # @return true iff success.  If false is returned, call getError() for error details.

    def encode(self, clearText):
        return True, self.sasl.wrap(clearText)

    # Decode data received from the server.
    #
    # @param cipherText Encrypted data received from the server
    # @param clearText (output) Decrypted clear text data 
    #
    # @return true iff success.  If false is returned, call getError() for error details.

    def decode(self, cipherText):
        return True, self.sasl.unwrap(clearText)

    # Get the user identity (used for authentication) associated with this session.
    # Note that this is particularly useful for single-sign-on mechanisms in which the 
    # username is not supplied by the application.
    #
    # @param userId (output) Authenticated user ID for this session.

    def getUserId(self):
        return self.attributes['externaluser']

    # Get the security strength factor associated with this session.
    #
    # @param ssf (output) Negotiated SSF value.

    def getSSF(self):
        return True

    # Get error message for last error.
    # This function will return the last error message then clear the error state.
    # If there was no error or the error state has been cleared, this function will output
    # an empty string.
    #
    # @param error Error message string

    def getError(self):
        error = self.lasterror[:]
        self.lasterror = ''
        return error



