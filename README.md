# Feeback App

This app is used as a package used for leaving feedback about your app. Users will tell you about what is right and what is wrong.



1. Run `pip install git+https://bitbucket.org/xenetix_software/xenetix_feedback_app/src/production/`
-------


2. Add "feedback", and "vote" to your INSTALLED_APPS setting like this:
-----------------------------------------------------------------------
```
    INSTALLED_APPS = [
        ...
        'feedback',
        'vote',
    ]
```
3. Add feedback email setting to your settings.py file:
-----------------------------------------------------
```
FEEDBACK_TO_EMAIL = ["dev@xenetixsoftware.com"]
```
-----------------------------------------------------
4. Add to your urls.py or routes.py.
------------------------------------
5. Run `python manage.py migrate` to create the feedback and vote models.
-------
6. Start the development server and visit http://127.0.0.1:8000/
---------------------------------------------------------------
7. Visit http://127.0.0.1:8000/feedback/ to start leaving feedback so you can tell the developers how much they suck. 
---------------------------------------------------------------------------------------------------------------------
8. If you use drf-flex-fields add this to your settings.py file:
---------------------------------------------------------
```
USER_SERIALIZER = "file_path.UserSerializer"
```
----------------------------------------------------------
Note: The vote function is a way for you to vote on feedback instances. Therefore, in order to vote on a particular feedback instance, the url will look like this:
/feedback/id/up_vote/ or /feedback/id/down_vote/
__________________________________________________

Only a super user can add feedback responses and change status on feedback.
