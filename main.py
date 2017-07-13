class ListHandler(webapp2.RequestHandler):
    def get(self):
        questions_query = Question.query().order(Question.questionText)
        list_of_questions = questions_query.fetch()
        
        template = jinja_environment.get_template('test_output.html')
        self.response.write(template.render(
        {
                'list': list_of_questions,
        }))

class SingleHandler(webapp2.RequestHandler):
    def get(self):
        question_id = self.request.get('id')
        question_id = int(question_id)
        single_question = Question.get_by_id(question_id)
        template = jinja_environment.get_template('single_test.html')
        self.response.write(template.render(
            {
                'question': single_question,
                'id' : question_id,
                

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
 
], debug=True)
