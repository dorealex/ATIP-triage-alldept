<h1>ATIP AI Demo</h1>
        <div>
            <h2>How to send requests:</h2>
            <p>Send requests to https://atip-triage-alldept.herokuapp.com/request/ .<br>
            Send a JSON request via POST. The response will be in the form: <strong>{'dept': 'result','pct': 0.XX%}</strong> where result is the abbreviation and pct is the percentage. The request format is as follows: <strong>{'text':'insert request text here'}</strong> <br>
            The user can also specify what they want by adding:
            <ul>
                <li>'what':'dept-only' will respond only with the department and the percentage. Will not chain(see below) </li>
                <li>'what':'prob_dept' will respond with a dict of all the departments who are above 0% in probabilities</li>
                <li>'what':'ised_sector' will respond with a dict of all the ised sectors and the %</li>
                <li>Not providing a specifier will provide the department, the percentage, and if the department happens to be ISED, it will chain the request and also provide a dict with the sectors</li>
            </ul>
            For examples of this in use, please see <a href='https://colab.research.google.com/drive/1zdn512if6NgA1PCyY5gqyf-GlkUskvPK'>this Google Colab notebook</a>
            </p>
        </div>
        <div>
            <h2>To-do:</h2>
    <ul>
        <li>Triage</li>
        <ul>
            <li>Departmental Triage</li>
            <ul>
                <li>AI Model - Done</li>
                <li>Web API - Done</li>
                <li>Front End for demo - In-Progress</li>
            </ul>
            <li>Sector Triage
                        <ul>
                <li>AI Model - Done</li>
                <li>Web API - Done</li>
                <li>Front End for demo - In-Progress</li>
            </ul>
            </li>

        </ul>

        <li>Retrieve</li>
            <ul>
                <li>POC - In-Progress</li>
                <li>Prototype</li>
                <li>Front End</li>
            </ul>
        <li>Redact</li>
            <ul>
                <li>POC - In-Progress</li>
                <li>Prototype</li>
                <li>Front End</li>
            </ul>
        <li>General</li>
            <ul>
                <li>Front End - In-Progress</li>
                <li>Navigation for Front End</li>
            </ul>
    </ul>
        </div>
