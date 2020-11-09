## Blog Post project

you will find .env file in this repository only for simplicity
to run this project, never put this file here to prevent security issues

### Start project
1) go to directory where docker-compose.yml located and 
    run `docker-compose up -d --build`
   
2) then go to `0.0.0.0:8125` to se if everything is running

3) to check if containers are running run `docker ps -a`

### Create a Super user
1) enter django container by running `docker exec -it blogpost_backend bash`

2) then run `python manage.py create_admin`, command will ask you to
    provide some credentials for admin user
   
3) after you create an admin user you can login to admin panel,
    go to `0.0.0.0:8125/admin` and enter your credentials that you provided before
   
### Create a post
got to admin panel to section `Posts`, and press Add post button,
fill required fields, press save
   
### Create post through API
1) first you need to have an admin user created
2) documentation provided here `https://app.swaggerhub.com/apis-docs/e424/Blog_post/1.0.0#/`

### Create a Visitor user
1) to leave a comment under a post you need to have Visitor 
   user created, go to main page and press Register button
   
2) fill required fields and pres save
