These are instructions to build and deploy a chatbot

Lex w/ Lambda is actually fairly simple.  In Lex, there are four basic items you need to understand:
Intent: An intent represents an action that the user wants to perform. You create a bot to support one or more related intents. i.e. OrderPizza
Utterances: How the user provokes an intent.  i.e. I want pizza
Slots: You add slots as part of the intent configuration. At runtime, Amazon Lex prompts the user for specific slot values. i.e. Crust Size, Toppings, etc
Slot Types: Each slot has a type. You can create your custom slot types or use built-in slot types. Each slot type must have a unique name within
  your account. i.e. Custom or AMAZON (Date/Time)

Step 1:
You create your Lexbot in the Lex console.  Define your utterances, intent, slots etc.

Step 2:
Prepare your Lambda function.  Once lex understands user’s sentence, it produces an input JSON. This input JSON goes to the code performing logic.
  Lex expects an output JSON in return. Both the input and output JSON have specific formats.
  You use the input event format here (https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html) to write your Lambda function
  Amazon Lex expects a response from a Lambda function in the following format: https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html#using-lambda-response-format

  Template Lambda Function includes a sns output to text and the python file is: chatbotsnsfunction.py

Step 3:
Once Lambda function is written, go back to Lex console and add it to either initialization/validation or fulfillment or both!  Test to confirm success.

Step 4: You need to make an s3 bucket with versioning turned on then:

-Launch the Cloud9 IDE
-In your Cloud9 workspace, clone the repository using git "git clone https://github.com/aws-samples/aws-lex-web-ui.git"
-cd into the root folder, aws-lex-web-ui
-npm install
-cd lex-web-ui
-npm install
-cd ../build
-./release.sh
-aws s3 mb s3://[your-lex-bootstrap-bucket-name] --region eu-west-1
-export BUCKET=[your-lex-bootstrap-bucket-name]
-./upload-bootstrap.sh

Step 5:
Download the master.yaml from the s3 bucket. Change the Bootstrap Bucket parameter to "[your-lex-bootstrap-bucket-name]" and change the Bootstrap Prefix to be just "artifacts"
Upload the master.yaml file to CloudFormation and Deploy!

Adjust parameters.  WebAppParentOrigin is usually something like: https://example.com:443

The CF deploys:

In Codebuild output, copy "WebAppBase" url

Step 6:
In Wordpress install plugins "Advanced iframe", "Popup Maker", and "Buttonizer".

  In Popup Maker:
  Create a new popup, choose "Form submission" and type [advanced_iframe src=""WebAppBase""]

  In Buttonizer:
  Create a new button and make the "Popup Maker" in "Button Action"
  Copy the code beneath "button action".. it should look something like this: a[href="#popupMakerWybx4ZmeeXeaI10P"]

  Go back to Popup Maker:
  In your Popup Settings, Go to triggers and add a new "Click to Open" trigger and copy and paste this code in "Extra CSS Selectors"

Verify chatbot is in your website and is operational.

Step 7:

Download and change css as necessary from webappbucket created.  The file is custom-chatbot-style.css
See this for help css guidance: https://github.com/aws-samples/aws-lex-web-ui/blob/master/README-css-style.md#iframe-width-and-height

Or popup maker is wp has its own styling.  You can do either or.
