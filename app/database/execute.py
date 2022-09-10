from database.commands import DBCommands
from database.connection import get_connection
commands = DBCommands()


async def execute_command(message, adduser=False, startchat=False, stopchat=False, chat=False, stopwaiting=False):
    conn = await get_connection()
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS users
    (
    telegram_id BIGINT PRIMARY KEY,
    in_waiting BOOLEAN,
    chatting_with BIGINT
    )
    """    
    )
    if adduser:
        await conn.execute(
            commands.ADD_NEW_USER,
            message.from_user.id
        )
    if startchat:
        row_request_user = await conn.fetchrow(
            commands.GET_USER,
            message.from_user.id
        )
        if row_request_user:
            if row_request_user["in_waiting"]:
                return 1
            elif not row_request_user["in_waiting"]:
                if row_request_user["chatting_with"]:
                    return 0
                else:
                    row = await conn.fetchrow(
                        commands.GET_USERS_WAITING
                    )
                    if row:
                        await conn.execute(
                            commands.CREATE_CHAT,
                            message.from_user.id,
                            row["telegram_id"]
                        )
                        await conn.execute(
                            commands.CREATE_CHAT,
                            row["telegram_id"],
                            message.from_user.id
                        )
                        return {
                            "request_user": message.from_user.id,
                            "chatting_with": row["telegram_id"]
                        }
                    else:
                        await conn.execute(
                            commands.SET_USERS_WAITING,
                            message.from_user.id
                        )
                        return 1
    if stopchat:
        row = await conn.fetchrow(
            commands.GET_USER,
            message.from_user.id
        )
        if row:
            if row['in_waiting']:
                return 1
            elif not row['in_waiting']:
                if not row["chatting_with"]:
                    return 0
                else:
                    await conn.execute(
                        commands.END_CHAT,
                        row["chatting_with"]
                    )
                    await conn.execute(
                        commands.END_CHAT,
                        message.from_user.id
                    )
                    return {
                        "request_user": message.from_user.id,
                        "chatting_with": row["chatting_with"]
                    }

    if stopwaiting:
        row = await conn.fetchrow(
            commands.GET_USER,
            message.from_user.id
        )
        if row:
            if row["in_waiting"]:
                await conn.execute(
                    commands.STOP_WAITING,
                    message.from_user.id
                )
            elif not row["in_waiting"]:
                if row["chatting_with"]:
                    return 1
                else:
                    return 0
    if chat:
        row = await conn.fetchrow(
            commands.GET_USER,
            message.from_user.id
        )
        if row:
            if row['in_waiting']:
                return 1
            elif not row['in_waiting']:
                if not row["chatting_with"]:
                    return 0
                else:
                    return {
                        "chatting_with": row["chatting_with"],
                        "message": message.text
                    }
    await conn.close()


