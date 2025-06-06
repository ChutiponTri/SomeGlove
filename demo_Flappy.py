import asyncio
from flappy.src.flappy import Flappy

# Function To Open Game
def flappy():
    asyncio.run(Flappy().start())

if __name__ == "__main__":
    flappy()
