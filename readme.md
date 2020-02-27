# ATIP AI Demo
## How to send requests:

Send requests to https://atip-triage-alldept.herokuapp.com/request/ .  
Send a JSON request via POST. The response will be in the form: **{'dept': 'result','pct': 0.XX%}** where result is the abbreviation and pct is the percentage. The request format is as follows: **{'text':'insert request text here'}**  
The user can also specify what they want by adding:

*   **'what':'dept-only'** will respond only with the department and the percentage. Will not chain(see below)
*   **'what':'prob_dept'** will respond with a dict of all the departments who are above 0% in probabilities
*   **'what':'ised_sector'** will respond with a dict of all the ised sectors and the %
*   Not providing a specifier will provide the department, the percentage, and if the department happens to be ISED, it will chain the request and also provide a dict with the sectors

For examples of this in use, please see [this Google Colab notebook](https://colab.research.google.com/drive/1zdn512if6NgA1PCyY5gqyf-GlkUskvPK)

## To-do:

* Triage
  * Departmental Triage
    * AI Model - Done
    * Web API - Done
    * Front End for demo - In-Progress
  * Sector Triage
    * AI Model - Done
    * Web API - Done
    * Front End for demo - In-Progress
  * Retrieve
    * POC - In-Progress
    * Prototype
    * Front End
  * Redact
    * POC - In-Progress
    * Prototype
    * Front End
  * General
    * Front End - In-Progress
    * Navigation for Front End
