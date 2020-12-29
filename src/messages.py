PERMISSION_DENIED_MESSAGE: str = "***PERMISSION DENIED!*** \n" \
                            "You are not permitted to use this command.  \n" \
                            "Please contact to your server master. \n."
ERROR_OCCURRED_MESSAGE: str = "***ERROR OCCURRED!*** \n" \
                              "Error has occurred while executing gcp request command. \n" \
                              "Please contact to your server master or the software developer. \n" \
                              "Error: {} \n"
OPERATION_COMPLETED_MESSAGE: str = "***Operation Completed! ***\n" \
                                   "Operation: {} has successfully completed. \n" \
                                   "This may take more 2~3 minutes that the Minecraft Server starts (stops)."
INSTANCE_IS_ALREADY_IN_REQUESTED_STATUS: str = "***Already in status of {}.*** \n" \
                                               "The instance is already in the status. \n" \
                                               "No operation has done."

PRE_STOP_OPERATION_PROCESSING: str = "Processing pre-stop operation... \n" \
                                  "Trying to shutdown Minecraft server from the console channel. \n" \
                                  "Whichever the operation is completed or not, " \
                                  "the server will shutdown in 5 minutes forcibly."

REQUEST_RECEIVED: str = "Operation: {} has requested. \n" \
                        "Please wait until the operation is done. \n"

START_REQUEST_RECEIVED_MESSAGE = "Trying to start the gcp server. \n" \
                                 "It takes 3 sec at least to complete the operation. \n" \
                                 "The minecraft server will start as soon as gcp server started. \n" \
                                 "PLEASE WAIT UNTIL YOU RECEIVE MESSAGE 'SERVER HAS STARTED!' " \
                                 "BEFORE YOU JOIN THE MINECRAFT SERVER."

STOP_REQUEST_RECEIVED_MESSAGE = "Trying to stop the gcp server. \n" \
                                 "It takes 5 minutes at least to complete the operation. \n" \
                                 "We will issue `stop` command in console channel. \n" \
                                 "And then, we will wait for 5 minutes for the Minecraft server stops." \
                                 "After all the process is done, we will shutdown GCP instance finally."
