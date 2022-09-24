#!/usr/bin/python3

import unittest
from httmock import urlmatch, HTTMock
import requests 
import responses 

'''
Retrieve all messages of a user or teams without any filters
 1. GET https://graph.microsoft.com/v1.0/users/{id}/chats/getAllMessages
 2. GET https://graph.microsoft.com/v1.0/teams/{id}/channels/getAllMessages 

Microsoft Graph API
  GET /me/chats
  GET /users/{user-id | user-principal-name}/chats
  GET /chats

  https://graph.microsoft.com/v1.0/me/chats?$top=1
'''

# define matcher :
@urlmatch(netloc=r'https://graph.microsoft.com/v1.0/me/chats?$top=1')
def google_mock(url, request):
  return 'feeling lucky?'

def test_mock(google_mock):
  # calling request
  r = requests.get('http://google.com')
  print(r.contest)

def get_req():
  print("Testing the get requests")

if __name__ == "__main__":
  print("testing google mock")
  test_mock(google_mock())




