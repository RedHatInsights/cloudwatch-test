# Example CloudWatch Openshift Application

This is a very simple application that logs a message to CloudWatch every 60
seconds. It's intended to be an example of the minimum configuration required
to configure an app to log to CloudWatch.  This example is in Python, so
obviously other languages will need to use other libraries, but the Openshift
configuration and CloudWatch conventions still apply.

Steps to deploy this app:

1. Get the AWS secret installed.  The app looks for `CW_AWS_ACCESS_KEY_ID` and
   `CW_AWS_SECRET_ACCESS_KEY`.

2. `oc create -f bc.yaml`.  This will install the build config and image
   stream.

3. `oc start-build -F cloudwatch-test`.  This will build the image.  The app
   should auto-deploy after the image is pushed to the image stream.

4. `oc logs $(oc get pod -l app=cloudwatch-test -o name)`.  This will print the
   logs from the script so you can see if it started up correctly.

5. Profit?  Go to your Kibana UI and see the logs!
