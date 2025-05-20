from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


async def get_filesystem_tools():
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",  # Arguments for the command
                "@modelcontextprotocol/server-filesystem",
                # TODO: IMPORTANT! Change the path below to an ABSOLUTE path on your system.
                "/path/to/your/folder",
            ],
        )
    )
    
    return tools
