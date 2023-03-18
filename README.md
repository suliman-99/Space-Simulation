# Space-Simulation
this is a program to simulate planets interactions

you can enter the planets data and the program will show you the expected scenario

there are a lot of features helps you save state and load it again and more to have a good experience with our program

there are a lot of ready demos may impress you !


# Main Idea
this program basically depends on:

1- ewton's law of universal gravitation

( F = (G * m1 * m2) / r^2 )

G: the gravitational constant

m1, m2: the masses of these two objects

r: the distance between the centers of the masses

F: the gravitational force acting between them

we use this Formula to calculate the force berween each pair of planets

-------------------------------------------

2- Newton's Second Law of Motion

( F = m * a ) => ( a = F / m )

m: mass of the object

F : Total Force applied on it

a: the acceleration of it

We Use this Fomula to calculate the acceleration of each planet depending on the total force applied on it

after that we can calculate the new velocity (speed vector) depending on the current velocity and the acceleration

after that we can calculate the new position (x, y, z) depending on the current position and the velocity

then we can re-render the object in the new place

we can do that a lot of time in the same seconde (more that 10 time) and we will have a good visualization
 
-------------------------------------------

# installation

first open cmd in the place you want to download the project in then write this commands :

1- git init

2- git pull https://github.com/suliman-99/Space-Simulation.git

3- pipenv install

4- pipenv shell

5- python main.py

enjoy it!

-----------------------------------------------

Feel free to use the code My Freind ^_^ .

If you know how to fix an issue, please open a pull request for it and I will be happy with your contribution.

Suliman Awad.
