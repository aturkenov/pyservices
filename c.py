import asyncio
from a import *
from b import *


if __name__ == '__main__':
    endpoint = SecondService.test.as_endpoint()
    output = asyncio.run(endpoint('10'))
    print(output)

