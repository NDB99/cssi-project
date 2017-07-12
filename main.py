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
import jinja2
import os

from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Question (ndb.Model):
    questionText = ndb.StringProperty()
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('question_input.html')
        self.response.write(template.render())
    def post(self):
        question_from_form = self.request.get('question')
        
        new_question = Question(questionText = question_from_form)
        question_key = new_question.put()
        
        template = jinja_environment.get_template('question_output.html')
        self.response.write(template.render(
        {
            'questionText': question_from_form
        }))

class ListHandler(webapp2.RequestHandler):
    def get(self):
        questions_query = Question.query()
        list_of_questions = questions_query.fetch()
        
        template = jinja_enviroment.get_template('question_output.html')
        self.response.write(template.render(
        {
                'list': list_of_questions,
        }))
        
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/list', ListHandler),
], debug=True)
