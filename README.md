# chenge
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.staging.yml up -d --build
    ```

    Test it out.

### Let's Encrypt Production

1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```
    fixtures:
    python manage.py dumpdata codehelp.Group codehelp.Category codehelp.List > fixtures/Data.json
    python manage.py loaddata fixtures/Data.json
    Test it out.
