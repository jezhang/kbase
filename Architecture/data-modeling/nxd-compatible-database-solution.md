
# Database changes process for Basic stage

During the basic stage of GXD rebuild project, TSC project team will delivery a lot of new features, and in the meanwhile TSC service team will apply some bugs fixing and changes to production of basic-lite.

In project team, it will have a lot of user stories need to change the database scheme, and in the service team also have some changes to be applied to the database schema.
 
The guideline

 * Database/kafka layer: use one compatible database schema;
 * Backend API layer: use different API version for incompabible changes;
 * WEB application layer: use BETA and Prod version;
 * Scanner application layer: preferred use API to display/hide functionality to the end user;

Base on the guideline we always deploy the latest database scheme and backend API service to DEV/INT/FAT/PROD environment.

This document will guide the delivery team how to handle the database changes and how to use one compatible database schema support the development of project and service team.

### Database changes on Project side

#### Estimate the impact to production

During the US presenation and estimation session, TSC team discussion and assess the changes whether impact production system and come to a conclusion which is a compatible change or incompatible change.

##### compatible change

No impact to the production system, directly apply the changes to database.

##### incompatible change

It will impact to the production system, and it will be performed in different sprints.

* Raise an user story to fix it on production for incompatible firstly;
* Deploy the fix user story on production;
* Continue the feature user story of Basic stage;

### Database changes on Service

Treat it as a new feature user story of basic stage.



### compatible changes



### incompatible changes



## User Story add field

## User Story modify field

## User Story remove field


## compatible changes


## incompatible changes


### Raise an user story

