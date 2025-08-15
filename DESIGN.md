# Design Report for this Application 

## What is the purpose of this app? 
I wanted to automate the process of sharing my projects in a blog-fashioned way. 

## Who are your main audience and how many per day? 
My main audiences are recuriters or aspiring junior developer like my self. I expect from 0-10 users per day (both concurrently/non-concurrently).  

## Design 

### Static Site Generator 
This website serves purpose of blog where each of my blog posts contains information about the program (README.md) and possibely contain design report where I motivate my technolgoy/design choices (DESIGN.md).  

The backend of this system, generating static site, works as follows: 
- Getting github repo data via making request concurrently 
- Using logic to convert markdown files into html file via multiple paralle process to speed up the process 

### Github Pages 
Github pages is a static site hosting service, allowing distrubting static site that will be generate by the backend of this system. So, ultimately Github pages will serve a purpose of Content Delivery Network (CDN). Considering relatively low number of expected (concurrent) user, this should be sufficient enough. 

#### Updating static sites 
The site is kept up-to-date automatically using GitHub Actions. A scheduled workflow runs daily, executing a script that fetches the latest data, rebuilds the static HTML files, and deploys the new version to GitHub Pages.

### Testing Strategy 
Since the app itself is quite straightforward, unit testing and end-to-end testing should be suffcicient enough. 

## Technologoy 

### Python
Python allows us to make concurrent request to GitHub API via asyncio, and multiple convertion processes can happen parallel via mulitpl-processing. On top of that, it is equipped with modules which allows converting .md files into .html which signfiicalntly boosts devlopment speed. 

### Github Action 
For CI/CD, we use Github action since it is well integrated with Github envrionments. 