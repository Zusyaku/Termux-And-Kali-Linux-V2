from proxy.http.parser import HttpParser, httpParserTypes, httpParserStates
from proxy.http.proxy import HttpProxyBasePlugin

class PluginBase(HttpProxyBasePlugin):
    '''Modified HttpProxyBasePlugin from proxy.py. Provides more functionality'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request  = HttpParser(httpParserTypes.REQUEST_PARSER)
        self.response = HttpParser(httpParserTypes.RESPONSE_PARSER)

    def before_upstream_connection(self, connection):
        return self.intercept_connection(connection)

    def handle_client_request(self, request):
        rtval = self.intercept_request(request)
        self.request = rtval
        return rtval

    def handle_upstream_chunk(self, chunk):
        self.response.parse(chunk.tobytes())
        if self.response.state == httpParserStates.COMPLETE:
            self.intercept_response(self.response)
        return memoryview(self.intercept_chunk(chunk.tobytes()))

    def on_upstream_connection_close(self):
        self.close_connection()

    def intercept_connection(self, conn):
        '''
            Intercept Connection. The `conn` argument represents
            HttpParser class from proxy.http.parser.

            Intercept the initial connection state and represent
            the data before the connection is actuall established.

            For TLS Interception, it would most probably be a
            CONNECT request. You can check host, port and other initials
            in this section.

            Modified/Orignal `conn` must be returned in this function.
            Returning `None` will drop the connection.
        '''
        return conn

    def intercept_request(self, request):
        '''
            Intercept Request. The `request` argument represents
            HttpParser class from proxy.http.parser

            Intercept the orignal request sent to the server. The
            request can be modified at this stage.

            You will see GET/POST/HEAD and other method requests
            here. You can modify the request body and other
            necessary details here.

            Modified/Orignal `request` must be returned in this function.
            Returning `None` will not send the request to the server.
        '''
        return request

    def intercept_chunk(self, chunk):
        '''
            Intercept chunks received from the server. The `chunk`
            argument represents built-in `bytes` object from
            python.

            Intercept response in chunks received from server.
            It is not in the final form yet. So, you can the received
            response here

            You will see mostly plain bytes in this section with what's
            incoming. This chunk from this function is then appended
            to response in `interept_response`.

            Modified/Orignal `chunk` must be returned in this function.
            Empty bytes object will append nothing to response
            Return `None` will cancel the response at that very moment.
        '''
        return chunk

    def intercept_response(self, response):
        '''
            Intercept response received from the server. The `response`
            argument represents HttpParser from proxy.http.parser.

            Intercept the response combined from the chunks received in
            `intercept_chunk` method. The response can only be viewed
            at this stage. It is not to be modified here

            NOTE: Changing or returning response here won't have any effect
            on the orignal response. For modifying response see
            `intercept_response` method.

            This function doesn't return anything.
        '''
        return response

    def close_connection(self):
        '''
            This methods gets called when the connection has been closed.
            It doesn't have arguments.

            The request and response both can be analyzed at this part
            and can be accessed at `self.request` and `self.response`
            respectively.

            The modifications in here won't mean anything. But you can
            deduce other results in this section.

            This function doesn't return anything and basically used for
            analysis.
        '''
        pass
