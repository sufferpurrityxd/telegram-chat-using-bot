class DBCommands:
    ADD_NEW_USER = \
        """
    INSERT INTO users(telegram_id, in_waiting) VALUES ($1, false) ON CONFLICT DO NOTHING
    """
    GET_USERS_WAITING = \
        """ 
    SELECT * FROM users WHERE in_waiting=true
        """
    SET_USERS_WAITING = \
        """
    UPDATE users SET in_waiting = true WHERE telegram_id=$1
        """
    CREATE_CHAT = \
        """
    UPDATE users SET in_waiting = false, chatting_with =$1 WHERE telegram_id=$2
        """
    END_CHAT = \
        """
    UPDATE users SET chatting_with=null WHERE telegram_id=$1
        """
    GET_USER = \
        """
    SELECT * FROM users WHERE telegram_id=$1
        """
