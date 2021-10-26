import setuptools

with open("README-pypi.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proxverter",
    version="0.5.3",
    author="hash3liZer",
    author_email="admin@shellvoide.com",
    description="Cross platform system wide proxy server & TLS Interception library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hash3liZer/Proxverter",
    project_urls={
        "Bug Tracker": "https://github.com/hash3liZer/Proxverter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: OS Independent",
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: System :: Networking :: Firewalls',
        'Topic :: System :: Networking :: Monitoring',
    ],
    packages=['proxverter', 'proxverter.plugins'],
    python_requires=">=3.7",
    install_requires=open('requirements.txt', 'r').read().strip().split("\n"),
    keywords=[
        'http, https, proxy, transparent proxy, web proxy, https proxy',
        'python3 web proxy, python3 https'
    ]
)
