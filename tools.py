from crewai_tools import YoutubeChannelSearchTool,YoutubeVideoTranscriptTool
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from tools import YoutubeVideoTranscriptTool
# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@handlename')

