![banner](https://user-images.githubusercontent.com/29171692/126787146-54fd3b6c-883b-4990-8cef-ba8816584bc4.png)

<p align="center"><img src="https://img.shields.io/static/v1?label=requirements&message=up%20to%20date&color=green&logo=list"/> <img src="https://img.shields.io/static/v1?label=python&message=%3E=3.7&color=blue&logo=python" /> <img src="https://img.shields.io/static/v1?label=docs&message=80%25&color=orange&logo=doc" /> <img src="https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey" /></p>

<h1 align="center">Proxverter</h1>
Cross platform system wide proxy server & TLS Interception library for Python. Basically a wrapper around proxy.py and PyOpenSSL allowing easy integration and certificate generation on command.

## Features
<ul>
  <li><b>Cross Platform</b>: The library is cross platform and can be used on windows, linux and macos</li>
  <li><b>HTTP Interception</b>: You can intercept, capture and cache HTTP traffic through this. </li>
  <li><b>TLS Interception</b>: It's a wrapper against lightweight <code>proxy.py</code> by <a href="https://github.com/abhinavsingh/">@abhinavsingh</a> which provides many features and TLS-interception being one of them</li>
  <li><b>Custom Plugins</b>: Through the API you can provide custom plugins to intercept and modify data as per your needs. Documentation regarding plugin development is given below</li>
  <li><b>System wide proxy</b>: The tool provides system wide proxy. You just have to call the API and the library will do the rest</li>
  <li><b>Certificate Generation</b>: You can generate self-signed certificate which is basically a wrapper around <code>pyopenssl</code></li>
  <li><b>Flexible</b>: The underlying code of Proxverter is documented and quite easy to understand and edit. The code can further be developer and reused easily. </li>
  <li><b>Lightweight</b>: Thanks to <code>proxy.py</code>, unlike <code>mitmproxy</code> and other interception tools, proxverter is lightweight and doesn't really carry that much space around. </li>
  <li><b>Logging</b>: Proper logging support with verbose mode. The modes when combined can be used to suppress errors as well</li>
  <li><b>Modifying data on the fly</b>: Since the library support TLS interception, the plugins can be used to modify data on the fly or reject any kind of request. </li>
</ul>

## Installation
### Requirements
Proxverter requires `openssl` for reading and managing private & public keys in certificates. Actually this is a dependency in `proxy.py` and we are hoping to have it removed soon with the usage of `pyopenssl`. Install openssl first:
```
$ choco install openssl      ## Windows
$ apt install openssl        ## Debian
$ yum install openssl        ## CentOS
$ brew install openssl       ## Mac OS
```

### Stable Release
```bash
$ pip3 install proxverter
```

### Development Version

```bash
$ git clone https://github.com/hash3liZer/Proxverter.git
$ cd Proxverter/
$ python3 setup.py install
```

## Getting Started
After installation, you should be able to import `proxverter` on your python terminal. As of now, the library has 2 major sub modules which are: `certgen` and `sysprox`. The use of both of them is disucussed in the later sections.

### HTTP Interception
```python
import proxverter
prox = proxverter.Proxverter(ip="127.0.0.1", port=8081, verbose=False)     ## Verbose mode will also show logs
prox.set_sysprox()                                                         ## Set system wide proxy
prox.engage()                                                              ## Press CTRL+C to move further
prox.del_sysprox()                                                         ## Remove system wide proxy
```

This will start proxy server in the background. Now, you can verify the working of proxy using `curl`:
```bash
$ curl -L -x 127.0.0.1:8081 http://www.google.com
```

### TLS Interception (HTTPS)
```python
import proxverter
prox = proxverter.Proxverter(ip="127.0.0.1", port=8081, is_https=True, verbose=False)    ## Verbose mode will also show logs

## Get certificate
prox.fetch_cert("/tmp/certificate.pem")                      

prox.set_sysprox()                                                         ## Set system wide proxy
prox.engage()                                                              ## Press CTRL+C to move further
prox.del_sysprox()                                                         ## Remove system wide proxy
```

The line `prox.fetch_cert` will generate a certificate at `/tmp/certificate.pem`. You need to import this certifcate in system root keychain or browser ceritifcates in order to capture TLS traffic.

Sometimes, you might want to get the `pfx` version of the certifcate to be imported in windows root keychain. You can get the `pfx` using following method:
```python
prox.fetch_pfx("/tmp/certificate.pfx")
```

Altough, there would be no need of private key for this to capture the traffic. However, if for some reason, you need private key as well. You can call the following method:
```python
prox.fetch_pkey("/tmp/key.pem")
```

The certificates and key are only generated for the first time the library is called. After that when you call the `engage` method, the previous certificates will be used. However, if you want to refresh certifcates and have newly generated certs, you have to pass the option `new_certs=True` to `Proxverter` instance:

```python
prox = proxverter.Proxverter(ip="127.0.0.1", port=8081, new_certs=True)
```

The TLS interception for SSL mode can be tested using this command:
```bash
$ curl -L -x 127.0.0.1:8081 https://www.google.com
```

### Interception with automatic system wide proxy
By default, when you call the `engage` method, proxvetrer will not automatically create a system wide proxy cache or in other words, you will have to setup the proxy yourself for the software you are targeting.

However, if you do want the proxverter to handle this case for you and create a system wide proxy cache i.e. traffic from the host will pass through our proxverter instance, you will have to pass the argument `sysprox=True` to `Proxverter` instance:

```python
import proxverter
prox = proxverter.Proxverter(ip="127.0.0.1", port=8081, sysprox=True)

prox.engage()
...
```

### Auto Import Certificate
**NOTE**: (Windows Only)

In the above section, we actually fetched the certificate using `fetch_cert` method and then imported it in system keychain for the proxy to be intercepted. Right? Now, proxverter can import this certificate into the system keychain automatically. This method is currently only supported for windows platform.

Note that, it only import the certificate in system keychain which means that every software which uses certificate from the system root store will work but eventually you still will have to import certificate in softwares which don't. An example is Firefox.

```python
import proxverter
prox = proxverter.Proxverter(ip="127.0.0.1", port=8081, is_https=True)

prox.import_cert()
```

### Verbose mode
Let's talk about logs from `proxy.py` tool. By default when the proxverter instance is created, all the logs are suppressed. However, you will be able to see the errors if occured any from `proxy.py`. For this we have argument: `verbose`. If you want to see the all the logs especially from `proxy.py`, you can set `verbose=True` in proxverter instance:

```python
import proxverter
prox = proxverter.Proxverter(ip="127.0.0.1", port=8081, verbose=True)
prox.engage()
```

## Generating Self Signed Certificates
Besides from TLS Interception, another purpose of `proxverter` is to generate certificates on command. This is different from the certificates and keys generated by `Proxverter` instance.

```python
from proxverter.certgen import Generator

gen = Generator()
gen.generate()         ## Generate certificate and stores in memory

gen.gen_key("/tmp/key.pem")     ## Public Certificate
gen.gen_cert("/tmp/cert.pem")   ## Private Key
gen.gen_pfx("/tmp/cert.pfx")    ## Certificate in PFX format to be be imported in windows keychain
```

This would generate credentials for a single certificate. If you need another certificate, you will need to create a separate instance. For example, if you want to generate 2 certificates, then:

```python
from proxverter.certgen import Generator

gen1 = Generator()
gen2 = Generator()

...
```

### Self Signed certificate with custom fields
A certificate accepts a number of fields like email, country, unit name etc. By default all these fields are left empty. However, you can specify these fields in `Generator` instance.

```python
from proxverter.certgen import Generator

gen = Generator(
  email="admin@shellvoide.com",
  country="PK",                      ## Country code here
  province="Islamabad Capital Territory",
  locality="Islamabad",
  organization="localhost",
  unit="localhost",
  commonname="example.com"
)
gen.generate()

...
```

## System wide proxy
Like other usages, `proxverter` can also be used to create a system wide proxy. This allows the host to forward all the traffic of the host to the proxy that was mentioned in system wide proxy instance.

```python
from proxverter.sysprox import Proxy

## Setting system wide proxy
sprox = Proxy(ip_address="127.0.0.1", port=8081)
sprox.engage()

...
## Do the stuff here while system wide proxy is on
...

## Removing system wide proxy
sprox.cleanup()
```

## Plugins
Now, plugins are an important part of **Proxverter**. In previous section, we only viewed how to tunnel system traffic through our proxy. But how to actually modify traffic? This is where plugins come into play. Before we further dive deep into plugins. I once again want to to thank abhinavsingh for all the major work on his project `proxy.py`. Let's start creating a new plugin. The plugin class is to be inherited by `PluginBase` and passed to `proxverter` instance:

```python
import proxverter
from proxverter.plugins import PluginBase

class CustomPlugin(PluginBase):

  def name(self):
    return "Custom Plugin for testing"

p = proxverter.Proxverter(
      "127.0.0.1",
      8800,
      is_https=True,
      plugins=[
        CustomPlugin
      ]
)

p.engage()
```

There are 5 major functions that we are going to see throughout the working of plugins and these are:
<ul>
  <li>Intercepting Requests: <code>intercept_request</code></li>
  <li>Intercepting Response: <code>intercept_response</code></li>
  <li>Intercepting Connection: <code>intercept_connection</code></li>
  <li>Intercepting Chunk: <code>intercept_chunk</code></li>
  <li>Connection Close: <code>close_connection</code></li>
</ul>

### Intercepting Requests
For requests we have `intercept_request` method. The function accepts one argument which is a `proxy.http.parser.HttpParser` instance and can be modified or changed at this stage. The argument holds different attributes and who's complete implementation can be seen through `help` in python terminal.

The function must return orignal/modified request object. Returning `None` will drop the request. Here's an example where we add a custom header to the request:
```python
class CustomPlugin(PluginBase):

  def intercept_request(self, request):
    request.add_header("Proxy", "Proxverter (@hash3liZer)")
    return request
```

### Intercepting Responses
For responses, we have `intercept_response` method. The function accepts one argument which is a `proxy.http.parser.HttpParser` instance. Unlike request, the response can't be modified at this stage. Even if it is modified, it won't mean anything. The function returns nothing and is called in the lifecycle of request when all the chunks from the server has been received.

Here's an example where we store the body of 404 response in a file:
```python
class CustomPlugin(PluginBase):

  def intercept_response(self, response):
    if response.code == b"404":
      fl = open("response.txt", "a")
      fl.write(str(response.body))
      fl.close()
```

### Intercepting Connection
Now, sometimes, you want to capture a connection instead of the sent request. This is the function where you can do that. The connection is the initial stage where the user tries to establish a connection with the targetted server. For TLS, you will have `CONNECT` requests here. The function accepts one argument which is a `proxy.http.parser.HttpParser` instance.

The function must return orignal/modified connection request. Here's an example where we only allow connections to google and drop otherwise:
```python
class CustomPlugin(PluginBase):

  def intercept_connection(self, conn_request):
    if "google.com" in conn_request.host:
      return conn_request

     return None  ## Drop the connection
```

### Intercepting Chunks
Previously, we saw how to intercept response. But we can't modify it there. To intercept a response, we need to do it when a chunk is received. The function has one argument which is of type `bytes` and can be modified. This chunk from here will then be forwarded to the client.

The function must return orignal/modified response chunk. Returning `None` will drop the connection response at any point. This is an example, where we modify the response of each request.
```python
class CustomPlugin(PluginBase):

  def intercept_connection(self, chunk):

    if self.response.state == 6   ## All chunks have been received
      return b"Response from proxverter"

    return b""  ## Append empty chunks
```

### Close Connection
In the lifecycle of a request, the final call would be `close_connection`. Altough, this function is merely for nothing and can be ignored for all but still you would find it quite useful in analysis scenarios. At this point of the cycle, the `self.request` and `self.response` attributes can be accessed to see what was sent and what was received in the cycle.
```python

class CustomPlugin(PluginBase):

  def close_connection(self):

    ## Request
    if self.request.method == "POST" and \
        self.request.host == "www.google.com" and \
        self.response.code == b"200":

        pass
```

## Known Issues
<ul>
  <li>Certificate wrapping errors when running in SSL mode. These errors can be ignored for now as they don't actually pose any misfunctionality at the moment.</li>
  <li>Suppressing errors when needed.</li>
</ul>

## What's Expected
<ul>
  <li>More desktop environments are to be supported in the upcoming version for linux. Currently the script deploys proxy settings for <code>Gsettings/Gconf</code> and <code>environment</code> variables. Other desktop environments including MATE and XFCE are not currently supported</li>
</ul>
