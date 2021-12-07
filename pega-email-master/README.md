<h1 align="center">
  <br>
  <a href="https://github.com/sobri3195/pega-email"></a>
</h1>

<h4 align="center">Find email addresses of Github users</h4>

<p align="center">
  <a href="https://github.com/sobri3195/pega-email/releases">
    <img src="https://github.com/sobri3195/pega-email">
  </a>
  <a href="https://github.com/sobri3195/pega-email">
    <img src="https://github.com/sobri3195/pega-email">
  </a>
  <a href="https://github.com/sobri3195/pega-email">
      <img src="https://github.com/sobri3195/pega-email">
  </a>
</p>

![demo](https://image.ibb.co/nenkff/Screenshot-2018-10-17-21-41-53.png)

#### Find email address of a user
`python pega-email.py username`

or

`python pega-email.py https://github.com/username`

#### Find email addressess of contributors of a repository
`python pega-email.py https://github.com/username/repository`


#### Find email addresses of members of an organization
`python pega-email.py organization --org`

or

`python pega-email.py https://github.com/orgs/organzation`

#### Save JSON output to a file
`python pega-email.py https://github.com/username/repository -o /path/to/file`

#### Rate limiting
Github allows 60 unauthenticated requests per hour but limit for authenticated requests is 6000 per hour.
You don't need to generate any kind of authenticated token, just supply your username via `-u` option as follows:

`python pega-email.py username -u yourUsername`

#### Threading
Pegasus Email supports multi-threading for faster data retrieval.

`python pega-email.py IBM --org -t 20`

#### Check if email has appeared in a breach
Pegasus Email uses haveibeenpwned.com API to check if an email has been breached or not. This feature is turned off by default and can be used with `--breach` option as follows

`python pega-email.py sobri3195 --breach`

#### Contributor
Muhammad Sobri Maulan
