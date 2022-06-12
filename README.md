# KZRecordsBot
This repository holds the source files behind the @KZRecords twitter bot.

### Background

CSGO or Counter Strike: Global Offensive is a popular FPS game on the PC. One of its defining features is the existence of community servers and community game-modes which are, as the name suggests, created and maintained by the community. A number of these game-modes take advantage of unique movement mechanics in the game engine, one of the most popular of these being Kreedz (named after the initial creator) which is often abbreviated to KZ. In this game-mode, a player attempts to get from one end of a map (which are themselves created by the community) to another in the fastest possible time, taking advantage of the unique movement mechanics in the game. You can think of it in some way as being like an obstacle course.

As with any game-mode with a timer, players compete to get the fastest time possible on given maps and a highly competitive KZ scene has been established over the years across multiple CounterStrike games, dating back to the original CounterStrike 1.6 all the way back in 2003. How world (often referred to as global) records are established differs across the different games and has even evolved over the years in CSGO as community members updated plugins and provided extra utility outside of the game. As it stands today, records are recorded automatically in game when a player sets a time on a whitelisted community server. This is done through the use of dedicated ecosystem of plugins and an API that provides a fairly sophisticated ecosystem. The existence in particular of the API allows for community members to quickly generate new tools for tracking and analysing records as well as player and map specific analytics. Some examples of these are the websites https://www.kzstats.com/, https://kzprofile.com/ and https://kzgo.eu/ which all provide leaderboards and player/map data.

### KZ Records Bot

While the above websites all provide extensive detail and are far more ambitious than this project, one thing they lack is a method of sending live updates to interested players when a map record has been beaten. Often this would just be for interest though sometimes a player may not see that someone has beaten their record unless someone tells them or they specifically go check on one of these websites.

As a result, a simple idea for a bot that hooked into the KZ API and provided a live (or pseudo-live) feed of records would fill a small niche, and given that twitter itself provides such a feed, has an already extensive user-base and has a very simple and modern API, it seemed like the natural choice to create a twitter bot to provide this service.

In full disclosure, this bot has primarily been developed as a learning tool, in particular to learn about docker and cloud hosting. As a result, the bot itself is relatively simple and the majority of the work is, for someone new to cloud hosting, in getting the bot up and running in an EC2 instance using docker containers. This is particularly difficult if you are using windows since you will have to navigate WSL2 to do so. I should note as well that a more efficient method of hosting would probably be to use an AWS lambda function, but that defeats the point of learning about containers and docker.

### Files

This repository contains 4 main files:
- app.py which is the main file of the project and contains the logic for the bot itself
- config.py which contains the logic for authenticating with twitter's API 
- Dockerfile, which is the dockerfile describing how the docker container image should be created
- requirements.txt which lists the python requirements that need to be installed by docker so that the script will run

### Updates and Maintenance

This project was primarily a proof of concept, it is currently running as expected and hence considered a success. It is unlikely support will be provided for this in the future if it does break.




