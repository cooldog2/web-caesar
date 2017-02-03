#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

# Helper's function to display same page when encrypted word is returned.
#Note: there is no input validation for 'Rotate by', server will generate error message wwhen field is blank
# (because program is looking for an integer).
def build_page(textarea_content):
        rot_label = "<label>Rotate by: </label>"
        rotation_input = "<input type = 'number' name = 'rotation'/> <br>"

        message_label = "<label>Type a message </label>"
        textarea = "<textarea name='message'>" + textarea_content + "</textarea> <br>"  #what user typed in

        submit = "<input type = 'submit'/>"
        form = ("<form method = 'post'>" +
                rot_label + rotation_input + "<br>" +
                message_label + textarea + "<br>" + submit + "</form>")

        header = "<h2> Web Caesar</h2>"

        return (header + form)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Call function; function is empty ("") because user has not yet inputted anything in textare box
        content = build_page("")
        self.response.write(content)

    def post(self):
        # video4: receiving request from form in GET function:
        # get key value pair; key is the message; value is what user typed in
        message = self.request.get("message")   # What user typed in
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation) # What user typed in (message and rotation)
        # encodes all special characters that may interperted as html and replaces character with encoded version
        escaped_message = cgi.escape(encrypted_message)
        # after program encrypts message, call the builSd_page function
        content = build_page(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
