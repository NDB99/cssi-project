#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
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
class Answer (ndb.Model):
    answerText = ndb.StringProperty()
    question = ndb.IntegerProperty()

    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('question_input.html')
        self.response.write(template.render())

    def post(self):
        question_from_form = self.request.get('question')
        
        new_question = Question(questionText = question_from_form)
        question_key = new_question.put()

        template = jinja_environment.get_template('question_confirm.html')
        self.response.write(template.render(
        {
            'questionText': question_from_form,
            'question_id': question_key.id()
        }))

class SingleHandler(webapp2.RequestHandler):
    def get(self):
        question_id = self.request.get('id')
        question_id = int(question_id)
        single_question = Question.get_by_id(question_id)

        template = jinja_environment.get_template('single_question.html')
        self.response.write(template.render(
            {
                'question': single_question,
                'id' : question_id, 

            }))

    def post(self):
        answer_from_form = self.request.get('answer')
        new_answer = Question(answerText = answer_from_form)
        answer_key = new_answer.put()

        template = jinja_environment.get_template('answer.html')
        self.response.write(template.render(
            {
                'answerText': answer_from_form, 
                'answer_id': answer_key.id(),

            }))

class ListHandler(webapp2.RequestHandler):
    def get(self):
        questions_query = Question.query().order(Question.questionText)
        list_of_questions = questions_query.fetch()
        
        template = jinja_environment.get_template('test_output.html')
        self.response.write(template.render(
        {
                'list': list_of_questions,
        }))


class AnswerHandler(webapp2.RequestHandler):
    def post(self):

        answer = self.request.get('answer')
        Id = int (self.request.get('id'))

        new_answer = Answer(answerText = answer, question = Id)
        answer_key = new_answer.put()

        answer_query = Answer.query(Answer.question == Id)
        list_of_answers = answer_query.fetch()
        
        template = jinja_environment.get_template('answer.html')
        self.response.write(template.render(
        {
                'Alist': list_of_answers,
        }))



class DeleteHandler(webapp2.RequestHandler):
    def post(self):
        question_id = self.request.get('id')
        question_id = int(question_id)
        question_to_delete = Question.get_by_id(question_id)
        question_to_delete.key.delete()
        self.redirect('/list')

        

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/list', ListHandler),
    ('/delete', DeleteHandler),
    ('/single', SingleHandler),
    ('/answer', AnswerHandler),
 
], debug=True)
