# BUILT-IN TOOLS

# from langchain_community.tools import DuckDuckGoSearchRun
#
# search_tools = DuckDuckGoSearchRun()
#
# result = search_tools.invoke("top 5 news of pakistan today")
# # print(result)
#
# print(search_tools.name)
# print(search_tools.description)
# print(search_tools.args)

# CUSTOM-TOOLS

from langchain_core.tools import tool

@tool
def add(a : int, b : int) -> int:
    """add two numbers"""
    return a + b

result = add.invoke({"a": 3, "b": 4})

print(result)
print(add.description)
print(add.args)
print(add.name)
