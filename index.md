# [yote](https://github.com/ides15/yote)

## Project Description
Tools like Google Docs are helpful for collaborating on documents in real-time but collaborative programming is usually only done through version control or by looking at the same screen while on person is typing. This usually works, but if you are a remote worker, then pair programming becomes difficult and inefficient. This project's goal would be to make pair programming easier by creating an interface like Google Docs designed and developed for programming.

## Project Design
I think the main obstacle I will have to figure out for this project is getting users connected to one "lobby" in order to work on each other's machines at the same time. As I'm in the process of figuring out the full structure of the project, I'm not sure *exactly* how I'll do this, but I want to practice my Python so I'll at least be using that. I may set up a URL that the original user receives that they can give to the other user to connect to the lobby. I'll be using Flask or Django for this, as they are the most popular Web frameworks for Python that I know of. For the interface that programmers use, I will start with Vim, as it is a command line interface and probably one of the simplest text editors that I know how to use. Using Vim is only for the proof-of-concept, and I will attempt to make this project work between different editors and programming environments so that programmers aren't constrained by specific editors and editor features.

The goal of this project is to allow multiple programmers to work on a piece of code at the same time, similar to how Google Docs does collaborative document editing. The use cases for this are to allow the user to easily set up a sharing session with other users (this includes the original user making the session and easily sharing it with the other users) and be able to edit code in real time with multiple users.

I'll be making a documentation folder in my repository page for things like usage and how to set up and share a session. If I can add to the project, I'll try and make plugins for different editors and programming environments, like I said in the second paragraph.

## Project Schedule
By Checkpoint 1, since I just finalized what I am doing for the project, I don't expect to have much done, but I'll look into how I'll set up the lobby and how multiple users can connect to that lobby easily.

By Checkpoint 2, I want to have the lobby mostly finished and allow users to send information between each other. I want the information to be sent in such a way that it will be intuitive to use that information in Vim to show separate users connected to the lobby.

By Checkpoint 3, I want to have figured out how I will track events from cursor movements and text inputs from the origin host in Vim and broadcast those events to all users in the lobby. After I implement the event tracking, I will figure out how to fire those events in the other users' instances of Vim.

The final project should be fully operational collaborative coding between multiple users through Vim. This includes the lobby session creation and Vim collaborative usage.

## Project Justification

### Novelty
I think this project is novel enough because there aren't many (if any) products that do this already. I think that the main reason there aren't products that do this is because version control has been so helpful in developing a product where you can locally make breaking changes to a codebase and it won't affect the codebase on other people's computers. The collaborative nature of this product is novel because it will be similar to Google Docs in that multiple people can work on code at the same time, but **only** on the original user's local code. This way, if the code breaks, it won't break everyone's code, just the original user's. This will also transform the way pair programming works because remote workers will be able to effectively and efficiently pair program without having to be in the same physical space.

### Complexity
This project will be complex because of 3 main things:
- lobby sessions
- security
- integration with editors

The lobby sessions will be difficult because there needs to be a way that users can **easily** connect to the same unique lobby and transmit information quickly through to all lobby members. This will require load balancing, some sort of web socket implementation, and it will all have to be done securely.

Security is very important for this project because private source code obviously can't be sent across the internet unprotected. Another reason is because the lobby sessions should only be reserved for users that the original user wants in that lobby, not random people that can edit the code however they want.

Integration with editors is the third main complexity with this project. Sending information between computers isn't hard, but doing it in a way that is fast and easily consumable by editors will be a challenge. I am only going to be using Vim at first due to Vim's simplicity and the fact that it is a command-line editor. Once the project works well with Vim, I can look into a more universal system that can work with multiple programming environments.
