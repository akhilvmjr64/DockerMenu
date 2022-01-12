# this is a class to create a form
class form:
    # we need to give the heading using attributes which will be displayed on the form
    heading=""
    # we need to specify the what input boxes must be created
    params={}
    # this is to specify where the form will go on submitting the page
    location=""
    # this is to specify what method we need to use for sending the input
    method=""
    # this is to specify what should be displayed on the submit button
    submit="Submit"
    def out(self):
        # if all the details are correctly provided then following will be executed
        if(len(self.params)!=0):
            print("<div class='form'>")
            print("<form action='{0}' method='{1}' {2}>".format(self.location,self.method.lower() if self.method.lower()!="" else "GET", self.params.get('formextra')))
            button=True
            print("<h1>{0}</h1>".format(self.heading))
            for i in self.params:
                if i!="formextra":
                    if(self.params[i]['type'].lower()=='select'):
                        print("<p>{0}</p><select name='{1}' >".format(i,self.params.get(i).get('name')))
                        print("<option selected disabled>Select {0}</option>".format(i))
                        print("<option disabled>{0}</option>".format(self.params.get(i).get('values')[0]))
                        for j in self.params.get(i).get('values')[1:]:
                            print("<option value='{0}'>{0}</option>".format(j))
                        print("</select>")
                    elif(self.params[i]['type'].lower()=='textarea'):
                        print("""
                            <p>{0}</p><textarea name='{2}' placeholder='Enter {0}...' {3}></textarea>
                        """.format(i,self.params.get(i).get('type'),self.params.get(i).get('name'),self.params.get(i).get('extra')))
                    else:
                        print("""
                            <p>{0}</p><input type='{1}' name='{2}' placeholder='Enter {0}...' {3}/><br>
                        """.format(i,self.params.get(i).get('type'),self.params.get(i).get('name'),self.params.get(i).get('extra')))
            if button:
                print("<input type='submit'>")
            print("</form>")
            print("</div>")        
        else:
            # will print error if there is anything required is missing in configuration during configuration
            print("<div class='form'>")
            print("<form action='{0}' method='{1}' {2}>".format(self.location,self.method.lower() if self.method.lower()!="" else "GET", self.params.get('formextra')))
            print("<h1 style='margin: 0px;'>{0}</h1>".format(self.heading))
            print("</form>")
            print("</div>") 