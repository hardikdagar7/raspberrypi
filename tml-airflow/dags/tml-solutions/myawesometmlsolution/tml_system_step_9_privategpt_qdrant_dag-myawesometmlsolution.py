from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.decorators import dag, task
import os 
import tsslogging
import sys

sys.dont_write_bytecode = True

######################################################USER CHOSEN PARAMETERS ###########################################################
default_args = {
 'owner': 'Sebastian Maurice',   # <<< *** Change as needed   
 'start_date': datetime (2023, 1, 1),   # <<< *** Change as needed   
 'retries': 1,   # <<< *** Change as needed   
}

############################################################### DO NOT MODIFY BELOW ####################################################
# Instantiate your DAG
@dag(dag_id="tml_system_step_9_privategpt_qdrant_dag_myawesometmlsolution", default_args=default_args, tags=["tml_system_step_9_privategpt_qdrant_dag_myawesometmlsolution"], start_date=datetime(2023, 1, 1), schedule=None,  catchup=False)
def startaiprocess():
    # Define tasks
    def empty():
        pass
dag = startaiprocess()    

    
def startprivategpt(**context):
     VIPERHOST=""
     VIPERPORT=""
     HTTPADDR=""
     repo=tsslogging.getrepo()
     tsslogging.tsslogit("PrivateGPT DAG in {}".format(os.path.basename(__file__)), "INFO" )                     
     tsslogging.git_push("/{}".format(repo),"Entry from {}".format(os.path.basename(__file__)),"origin")                
    
     with open(basedir + "/Viper-produce/admin.tok", "r") as f:
        VIPERTOKEN=f.read()

     if VIPERHOST=="":
        with open(basedir + '/Viper-produce/viper.txt', 'r') as f:
          output = f.read()
          VIPERHOST = HTTPADDR + output.split(",")[0]
          VIPERPORT = output.split(",")[1]

     context['ti'].xcom_push(key='VIPERTOKEN',value=VIPERTOKEN)
     context['ti'].xcom_push(key='VIPERHOST',value=VIPERHOST)
     context['ti'].xcom_push(key='VIPERPORT',value=VIPERPORT)
     context['ti'].xcom_push(key='HTTPADDR',value=HTTPADDR)