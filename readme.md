# [github.com/ides15/yote](https://github.com/ides15/yote)

## Project Description
Tools like Google Docs are helpful for collaborating on documents in real-time but collaborative programming is usually only done through version control or by looking at the same screen while on person is typing. This usually works, but if you are a remote worker, then pair programming becomes difficult and inefficient. This project's goal would be to make pair programming easier by creating an interface like Google Docs designed and developed for programming.

## Project Design
I think the main obstacle I will have to figure out for this project is getting users connected to one "lobby" in order to work on each other's machines at the same time. As I'm in the process of figuring out the full structure of the project, I'm not sure *exactly* how I'll do this, but I want to practice my Python so I'll at least be using that. I may set up a URL that the original user receives that they can give to the other user to connect to the lobby. I'll be using Flask or Django for this, as they are the most popular Web frameworks for Python that I know of. For the interface that programmers use, I will start with a web interface, as it is a common interface that people know how to use and probably one of the easiest ways to collaborate over an internet. Using the web interface is only for the proof-of-concept, and I will attempt to make this project work between different editors and programming environments so that programmers aren't constrained by specific applications and editor features.

The goal of this project is to allow multiple programmers to work on a piece of code at the same time, similar to how Google Docs does collaborative document editing. The use cases for this are to allow the user to easily set up a sharing session with other users (this includes the original user making the session and easily sharing it with the other users) and be able to edit code in real time with multiple users.

I'll be making a documentation folder in my repository page for things like usage and how to set up and share a session. If I can add to the project, I'll try and make plugins for different editors and programming environments, like I said in the second paragraph.

## Project Schedule
By Checkpoint 1, since I just finalized what I am doing for the project, I don't expect to have much done, but I'll look into how I'll set up the lobby and how multiple users can connect to that lobby easily. I also want to be able to send files between users so that all users have a starting file to work from. This will be established through a CLI and an API, and the starting file(s) will be persisted in a sqlite database.

By Checkpoint 2, I want to have the lobby set up in the following fashion:
- CLI command to allow users to connect to a lobby specific to their session URL
- lobby unique to a specific session URL (only users with the specific session URL can connect to that lobby)
- users can "chat" through that lobby (I'm not building a chat application, but a chat app is very similar in terms of the lobby system I want to implement so I'll just have the chat app working by Checkpoint 2)

I also want to have a frontend set up by Checkpoint 2 that allows a user to generate a session URL that the user can distribute to other users so that they can join a common session. That URL will then be used to join a unique lobby (see the previous paragraph). This frontend will also have various links to my github page and other social pages.

By Checkpoint 3, I will have created a web interface for users to connect to so they can have a place to edit code. The connecting to this interface will be done by a landing page (which gives the user a place to either generate a session or join an existing session) and a coding page (includes an editor and a list of all people connected to the server). Users will be able to write code on this editor and the changes to this code will be reflected in the editors of all other clients connected to that session.

The final project should be operational collaborative coding between multiple users (similar to Google Docs). This includes the lobby session creation and collaborative usage. The lobby should be unique and only accept users who have the correct session URL.

## Finished Project Remarks
After finishing this project, I looked back on my initial goals for this project. I wanted to make a "Google Docs"-like interface to aid programmers in pair programming remotely. I think I have made a good representation of what I want the program to do. Users can generate sessions to work on code and other users can join those sessions to work on code together. Changes made on one user's editor will be reflected in all other users' editors in real time. Users connected to one session won't be able to edit code in other sessions, or vice-versa.

I wanted to add things like authentication, more language support, the ability to load files from a user's filesystem, and the ability to download completed files onto the user's filesystem. Also, originally I wanted to make a lower-level CLI API for key-bindings for editors to make their own real time "Google Docs"-like interface, but revised my proposal so that it would be easier to demonstrate for the class's purposes and to actually have something visible for the final presentation.

## Project Justification

### Novelty
I think this project is novel enough because there aren't many (if any) products that do this already. I think that the main reason there aren't products that do this is because version control has been so helpful in developing a product where you can locally make breaking changes to a codebase and it won't affect the codebase on other people's computers. The collaborative nature of this product is novel because it will be similar to Google Docs in that multiple people can work on code at the same time, but **only** on the original user's local code. This way, if the code breaks, it won't break everyone's code, just the original user's. This will also transform the way pair programming works because remote workers will be able to effectively and efficiently pair program without having to be in the same physical space.

### Complexity
This project will be complex because of 3 main things:
- lobby sessions
- security
- event tracking

The lobby sessions will be difficult because there needs to be a way that users can **easily** connect to the same unique lobby and transmit information quickly through to all lobby members. This will require load balancing, some sort of web socket implementation, and it will all have to be done securely.

Security is very important for this project because private source code obviously can't be sent across the internet unprotected. Another reason is because the lobby sessions should only be reserved for users that the original user wants in that lobby, not random people that can edit the code however they want.

Event tracking is the third main complexity with this project. Sending information between computers isn't hard, but finding the information to send and doing it in a way that is fast and easily consumable will be a challenge. I am only going to be using a web interface at first due to it's simplicity and the fact that it is an established way of people to collaborate over an internet. Once the project works well with the web interface, I can look into a more universal system that can work with multiple programming environments.

### Usage
To download the code and all dependencies:

`git clone https://github.com/ides15/yote.git`

`cd yote`

`pip3 install -r requirements.txt`

To run the application:
- In Terminal #1:

    `python3 lobby/server.py`
- In Terminal #2:

    `python3 api.py`

Navigate to `file:///<place the project is stored>/frontend/index.html` in your browser.

NOTE: because this project is hosted locally and requests to the API will be met with an `Access-Control-Allow-Origin` headers warning, there needs to be a way to bypass the CORS problem. In Google Chrome, I am using the [Allow-Control-Allow-Origin: * extension]("https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi"). In Firefox, the error doesn't happen.
