# Databricks notebook source
# DBTITLE 1,Install Python Libraries (Serverless)
# MAGIC %pip install dbt-databricks

# COMMAND ----------

# DBTITLE 1,Restart the Python Session
dbutils.library.restartPython()

# COMMAND ----------

# DBTITLE 1,Verify DBT Setup and Connection to Serverless
# The dbt debug command is a diagnostic tool used to check the setup and configuration of your dbt project, ensuring that everything is correctly set up for a successful connection to your data warehouse and proper functioning of your dbt environment.  It checks your profiles.yml and dbt_project.yml files for any configuration errors and tests the connection to the serverless sql warehouse.

!dbt debug

# COMMAND ----------

# DBTITLE 1,Execute DBT Model Tests
# The dbt test command is used to execute data tests that validate the integrity and correctness of data in your transformation models. These tests are vital for ensuring that your data transformations meet expected business rules and maintain data quality.

#Testing Data Assertions: dbt test runs assertions on your data models. These tests can be custom SQL queries or predefined test types such as unique, not_null, accepted_values, etc. Each test is defined within your dbt project and is aimed at verifying specific aspects of your data.

!dbt test

# COMMAND ----------

# DBTITLE 1,Deploy DBT Models
# The dbt run command is a core component of dbt's functionality, used to execute the data transformation models defined in your dbt project. 

# When you execute dbt run, dbt first compiles the SQL models in your project. This involves converting the Jinja-templated SQL code into raw SQL that can be executed against your data warehouse. This step also resolves any dependencies between models to determine the order in which they should be run based on their references to each other.

# After compilation, dbt executes the resulting SQL scripts in the order determined by the dependencies. Each model represents a transformation step, often materializing the output as a table or view in the data warehouse. dbt run handles the full lifecycle of these transformations, ensuring that each model is built or rebuilt according to the specifications in the project.

!dbt run
