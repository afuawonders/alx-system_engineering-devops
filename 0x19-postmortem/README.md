# My Initial Postmortem Analysis
An assessment of a debugging task

## Summary
On September 11, 2018, between 0900 and 1300 PST, a Wordpress website hosted on a LAMP stack encountered a critical issue, resulting in a 500 Internal Server Error. All users were affected due to a typographical error in the /var/www/html/wp-settings.php file.

## Timeline
- 0900: Initial user report of a 500 error on Chrome. Verified the issue using `curl -sI localhost`.
  (https://cdn-images-1.medium.com/max/1600/1*DsPxPOf6xfNCwYa_MJOKDw.png)

- 1000: Diagnosed the problem by inspecting running processes and system calls for the apache2 process under the www-data user. Utilized `ps aux` and `strace` commands.
  (https://cdn-images-1.medium.com/max/1600/1*SxSwxTsw2Rx-HxPYuvlCFg.png)

- 1030: Ran `curl localhost` separately to display strace results, revealing a typo in a php filename within one of the script files.
  (https://cdn-images-1.medium.com/max/1600/1*fgYknIpdzxuSyndtoQ3-MA.png)

- 1100: Enabled debug mode in /var/www/html/wp-config.php to scrutinize all php scripts.
  (https://cdn-images-1.medium.com/max/1600/1*i2FuDtxjrkVIFL_uc7v9pA.png)

- 1115: Ran `curl localhost` again, confirming the typo on line 137 of /var/www/html/wp-settings.php.
  (https://cdn-images-1.medium.com/max/1600/1*MpUTbKt3TJW6U7FrtMNbDw.png)

- 1116:Identified and corrected the typo on line 137 of /var/www/html/wp-settings.php.
  (https://cdn-images-1.medium.com/max/1600/1*7xgt1Xdw7TZ2aXKlZ1Om5A.png)

- 1200: Developed a puppet script to replace the erroneous string with the correct one and executed the script.
  (https://cdn-images-1.medium.com/max/1600/1*JFtXiPcFFCn78OunWL7i3w.png)
  (https://cdn-images-1.medium.com/max/1600/1*CyzxODjZd2T6XZoNetRtKA.png)

- 1215: Confirmed the resolution by checking the status of a GET request. The website returned a 200 HTTP status code.

- 1300: Submitted the script, closing the case.

## Root Cause
A typo on line 137 of /var/www/html/wp-settings.php:
`require_once(/var/www/html/wp-includes/calss-wp-locale.phpp)`
should be
`require_once(/var/www/html/wp-includes/calss-wp-locale.php)`

## Resolution
- Developed a puppet script utilizing the `sed` command to replace the erroneous string with the correct one.

## Corrective/Preventive Measures
- Enable debug mode in /var/www/html/wp-config.php before deploying the website to identify and rectify errors beforehand, enhancing customer satisfaction.
- Monitor host metrics in SumoLogic to confirm site activity, with a lack of activity signaling potential issues.
- Regularly check the web server's status and monitor uptime.
- Keep an eye on request and response rates to ensure optimal website performance.
- Monitor traffic and CPU load, identifying idle threads and less popular pages to enhance the website's interface, content, and functionality for a broader audience.
