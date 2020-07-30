# Others
# all_symptoms = open('Others/Symptoms.txt')
# symptoms = []
# for symptom in all_symptoms:
#     symptoms.append(symptom[:-1])
# text = '@Rule(Fact(action = \'find_disease\')'
# extra_1 = '''
# def not_matched(self, '''
# extra_2 = '''):
#     print("\\nDid not find any disease that matches your exact symptoms")
#     lis = ['''
# for symptom in symptoms:
#     text = text + ', Fact(' + symptom + ' = MATCH.' + symptom + ')'
# text = text + ', NOT(Fact(disease = MATCH.disease)), salience = -999)' + extra_1
# sym_list = ''
# counter = 0
# for symptom in symptoms:
#     if counter == 0:
#         sym_list = sym_list + symptom
#         counter = counter + 1
#     else:
#         sym_list = sym_list + ', ' + symptom
# text = text + sym_list + extra_2 + sym_list + ']'
# print(text)

# Rules
# import os
# disease_list = os.listdir('Disease Symptoms')
# all_symptoms = open('Others/Symptoms.txt')
# first = '''@Rule(Fact(action = 'find_disease')'''
# second = ''')
# def disease_'''
# third = '''(self):
#     self.declare(Fact(disease = "'''
# counter = 0
# symptoms = []
# for symptom in all_symptoms:
#     symptoms.append(symptom[:-1])
# for disease_txt in disease_list:
#     name = 'Disease Symptoms/' + disease_txt
#     disease = open(name)
#     text = first
#     y_ns = []
#     for line in disease:
#         y_ns.append(line[:-1])
#     if len(y_ns) != 0:
#         for i in range(len(y_ns)):
#             text = text + ', Fact(' + symptoms[i] + ' = "' + y_ns[i] + '")'
#         text = text + second + str(counter) + third + disease_txt[:-4] + '"))'
#         counter = counter + 1
#         print(text)

# Symptoms
# all_symptoms = open('Others/Symptoms.txt')
# counter = 0
# for symptom in all_symptoms:
#     symptom = symptom[:-1]
#     first_text = '''@Rule(Fact(action = 'find_disease'), NOT(Fact('''
#     second_text = ''' = W())), salience = 1)
# def symptom_'''
#     third_text = '''(self):
#     self.declare(Fact('''
#     fourth_text = ''' = '''
#     fifth_text = ''']))'''
#     symptoms_txt = open('Symptoms.txt', 'a')
#     symptoms_txt.write(first_text + symptom + second_text + str(counter) + third_text + symptom + fourth_text
#                        + 'prog_input[' + str(counter) + fifth_text + '\n')
#     symptoms_txt.close()
#     counter = counter + 1

# API
# all_symptoms = open('Others/Symptoms.txt')
# counter = 0
# for symptom in all_symptoms:
#     symptom = symptom[:-1]
#     print(symptom + ' = str(request.args.get(\'' + symptom + '\'))')

