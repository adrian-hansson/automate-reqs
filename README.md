# README

## Instructions

1. Create technical documentation for a software project, with a focus on defining a software architecture based on requirement analysis.
2. Analyze a list of requirements and determine if those requirements describe or imply that an integration between two systems is needed to satisfy the requirement. If any integrations are found, they should be added to the list of integrations.
   1. Use natural language processing to analyze the requirements.
   2. Algorithms or rules to determine if any integrations are required between services or applications based on the analyzed requirements. This step involves pattern matching, keyword extraction, or even machine learning approaches if you have labeled data indicating integration needs. For example, you could search for keywords like "communicate," "exchange data," or specific service names within the requirements to identify integration points.
3. Analyze a list of requirements and determine if those requirements describe or imply the use of any particular system (an application, service, external API, etc.). If any systems are identified, they should be added to the list of systems.
4. This should be achieved with a Python script which analyzes existing data in an Excel file.
5. Reading data is done from "data/input/data.xlsx"
6. Writing data is done by coping "data/input/data.xlsx" to "data/output/data_yyy-MM-dd_hh-mm-ss.xlsx" and modifying that file.

## Technology

List of technology to be used for implementation.

* Python
  * pandas
  * other useful libraries if needed
* Excel
* AI

## Data model

### Requirements

Read/write requirements data from/to the sheet called "requirements" in an Excel file called "data/input/data.xlsx".

Column | Description
------ | -----------
Requirement number | Unique number for each requirement
Title | The name and description of the requirement
Status | The status of the requirement. If value includes "Cancelled", then ignore the requirement.
Requirement category | Denotes the type of requirement. Useful for sorting.
Capability | Denote which system capability the requirement is related to.

### Integrations

Read/write integrations data from/to the sheet called "integrations" in an Excel file called "data/input/data.xlsx".

Column | Description
------ | ------------
source | The source system that triggers the integration
target | The target system being called in the integration
method | Denotes the method of integration, like HTTP or File
trigger | Denotes a description or event name of the trigger in the source system
action | A description of what the integration does
requirement | An optional reference to a "Requirement number" to denote which requirement needs to integration to be fulfilled

### System

Read/write systems data from/to the sheet called "systems" in an Excel file called "data/input/data.xlsx".

Column | Description
------ | ------------
id | The id of the system, formatted like "exampleApiService"
name | The name of the system, formatted like "Example Api Service"
parent | An optional reference to another system ID, if the system is only a part of a larger system.
