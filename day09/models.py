from sqlalchemy import Column,Integer,String
from database import Base

class ChatHistory(Base):
    __tablename__ = "chat_History"


    id = Column(Integer,primary_key = True,index=True)
    agent_name = Column(String,index=True)
    user_message = Column(String)
    ai_replay = Column(String)