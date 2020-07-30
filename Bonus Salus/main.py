from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}


def preprocess():
    global diseases_list, diseases_symptoms, symptom_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()


def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]


def if_not_matched(disease):
    print("The most probable disease that you have is %s\n" % disease)


def accept_input(input_array):
    symptoms = open('Others/Symptoms.txt')
    length = len(symptoms.readlines())
    if len(input_array) == length:
        return input_array


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), NOT(Fact(Bleeding=W())), salience=1)
    def symptom_0(self):
        self.declare(Fact(Bleeding=prog_input[0]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Blindness=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(Blindness=prog_input[1]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Blisters_Lesions=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(Blisters_Lesions=prog_input[2]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Bloating_Flatulence=W())), salience=1)
    def symptom_3(self):
        self.declare(Fact(Bloating_Flatulence=prog_input[3]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Discomfort_genitals=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(Discomfort_genitals=prog_input[4]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Chills_Shivering=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(Chills_Shivering=prog_input[5]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Confusion_intellect_impairment=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(Confusion_intellect_impairment=prog_input[6]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Cough=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(Cough=prog_input[7]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Cough_blood_Sputum=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(Cough_blood_Sputum=prog_input[8]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Deafness=W())), salience=1)
    def symptom_9(self):
        self.declare(Fact(Deafness=prog_input[9]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Dehydration=W())), salience=1)
    def symptom_10(self):
        self.declare(Fact(Dehydration=prog_input[10]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Fatigue_Tiredness=W())), salience=1)
    def symptom_11(self):
        self.declare(Fact(Fatigue_Tiredness=prog_input[11]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Fever=W())), salience=1)
    def symptom_12(self):
        self.declare(Fact(Fever=prog_input[12]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Headaches=W())), salience=1)
    def symptom_13(self):
        self.declare(Fact(Headaches=prog_input[13]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Loss_appetite=W())), salience=1)
    def symptom_14(self):
        self.declare(Fact(Loss_appetite=prog_input[14]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Loss_Smell=W())), salience=1)
    def symptom_15(self):
        self.declare(Fact(Loss_Smell=prog_input[15]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Malaise=W())), salience=1)
    def symptom_16(self):
        self.declare(Fact(Malaise=prog_input[16]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Nausea=W())), salience=1)
    def symptom_17(self):
        self.declare(Fact(Nausea=prog_input[17]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Numbness=W())), salience=1)
    def symptom_18(self):
        self.declare(Fact(Numbness=prog_input[18]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Pain=W())), salience=1)
    def symptom_19(self):
        self.declare(Fact(Pain=prog_input[19]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Paralysis=W())), salience=1)
    def symptom_20(self):
        self.declare(Fact(Paralysis=prog_input[20]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Poor_impaired_Vision=W())), salience=1)
    def symptom_21(self):
        self.declare(Fact(Poor_impaired_Vision=prog_input[21]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Rash_Redness_Swelling_Itching=W())), salience=1)
    def symptom_22(self):
        self.declare(Fact(Rash_Redness_Swelling_Itching=prog_input[22]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Restlessness=W())), salience=1)
    def symptom_23(self):
        self.declare(Fact(Restlessness=prog_input[23]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Runny_Stuffy_nose=W())), salience=1)
    def symptom_24(self):
        self.declare(Fact(Runny_Stuffy_nose=prog_input[24]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Seizures=W())), salience=1)
    def symptom_25(self):
        self.declare(Fact(Seizures=prog_input[25]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Shortness_Difficulty_breathing=W())), salience=1)
    def symptom_26(self):
        self.declare(Fact(Shortness_Difficulty_breathing=prog_input[26]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Sneezing=W())), salience=1)
    def symptom_27(self):
        self.declare(Fact(Sneezing=prog_input[27]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Sore_throat=W())), salience=1)
    def symptom_28(self):
        self.declare(Fact(Sore_throat=prog_input[28]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Stiff_neck=W())), salience=1)
    def symptom_29(self):
        self.declare(Fact(Stiff_neck=prog_input[29]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Stooling=W())), salience=1)
    def symptom_30(self):
        self.declare(Fact(Stooling=prog_input[30]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Sweating=W())), salience=1)
    def symptom_31(self):
        self.declare(Fact(Sweating=prog_input[31]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Swollen_lymphs=W())), salience=1)
    def symptom_32(self):
        self.declare(Fact(Swollen_lymphs=prog_input[32]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Vaginal_Penile_discharge=W())), salience=1)
    def symptom_33(self):
        self.declare(Fact(Vaginal_Penile_discharge=prog_input[33]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Vomiting=W())), salience=1)
    def symptom_34(self):
        self.declare(Fact(Vomiting=prog_input[34]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Weight_Loss=W())), salience=1)
    def symptom_35(self):
        self.declare(Fact(Weight_Loss=prog_input[35]))

    @Rule(Fact(action='find_disease'), NOT(Fact(Yellowing=W())), salience=1)
    def symptom_36(self):
        self.declare(Fact(Yellowing=prog_input[36]))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="Yes"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="Yes"), Fact(Loss_Smell="No"), Fact(Malaise="No"),
          Fact(Nausea="Yes"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="Yes"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_0(self):
        self.declare(Fact(disease="Appendicitis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="Yes"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="Yes"), Fact(Fever="No"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="Yes"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="Yes"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_1(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="Yes"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="No"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="No"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_2(self):
        self.declare(Fact(disease="Athletes_Foot"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="Yes"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="Yes"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="Yes"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="Yes"),
          Fact(Vaginal_Penile_discharge="Yes"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_3(self):
        self.declare(Fact(disease="Chlamydia"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="Yes"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="Yes"), Fact(Fever="No"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="No"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="Yes"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="Yes"), Fact(Sore_throat="Yes"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_4(self):
        self.declare(Fact(disease="Common_cold"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="Yes"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="Yes"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="Yes"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_5(self):
        self.declare(Fact(disease="Diarrhea"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="Yes"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="Yes"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_6(self):
        self.declare(Fact(disease="Enteriris "))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="Yes"), Fact(Fever="Yes"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="Yes"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="Yes"), Fact(Sneezing="Yes"),
          Fact(Sore_throat="Yes"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_7(self):
        self.declare(Fact(disease="Flu"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="Yes"), Fact(Fatigue_Tiredness="No"), Fact(Fever="No"),
          Fact(Headaches="No"), Fact(Loss_appetite="Yes"), Fact(Loss_Smell="No"), Fact(Malaise="No"),
          Fact(Nausea="Yes"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="Yes"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="Yes"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_8(self):
        self.declare(Fact(disease="Gastritis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="Yes"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="Yes"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="Yes"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="Yes"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="Yes"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_9(self):
        self.declare(Fact(disease="Gastroenteritis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="Yes"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="Yes"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="No"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="Yes"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_10(self):
        self.declare(Fact(disease="Gonorrhea"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="No"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="Yes"),
          Fact(Nausea="Yes"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="Yes"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="Yes"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_11(self):
        self.declare(Fact(disease="Heart_Disease"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="Yes"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="Yes"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="Yes"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_12(self):
        self.declare(Fact(disease="Herpes"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="Yes"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="Yes"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="Yes"),
          Fact(Nausea="No"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="Yes"), Fact(Stiff_neck="No"), Fact(Stooling="Yes"),
          Fact(Sweating="Yes"), Fact(Swollen_lymphs="Yes"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"),
          Fact(Weight_Loss="Yes"), Fact(Yellowing="No"))
    def disease_13(self):
        self.declare(Fact(disease="HIV"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="Yes"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"),
          Fact(Nausea="Yes"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="Yes"),
          Fact(Sweating="Yes"), Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="Yes"),
          Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_14(self):
        self.declare(Fact(disease="Malaria"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="Yes"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="Yes"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="Yes"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="Yes"), Fact(Loss_Smell="No"), Fact(Malaise="No"),
          Fact(Nausea="Yes"), Fact(Numbness="No"), Fact(Pain="No"), Fact(Paralysis="Yes"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="Yes"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="Yes"), Fact(Stooling="No"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="Yes"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_15(self):
        self.declare(Fact(disease="Meningitis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="Yes"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="Yes"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_16(self):
        self.declare(Fact(disease="PID"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="Yes"),
          Fact(Confusion_intellect_impairment="Yes"), Fact(Cough="No"), Fact(Cough_blood_Sputum="Yes"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="Yes"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="Yes"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="Yes"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="Yes"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="Yes"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_17(self):
        self.declare(Fact(disease="Pneumonia"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="No"), Fact(Loss_Smell="Yes"), Fact(Malaise="No"),
          Fact(Nausea="No"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="Yes"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="Yes"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_18(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="Yes"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="No"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="Yes"),
          Fact(Nausea="No"), Fact(Numbness="Yes"), Fact(Pain="No"), Fact(Paralysis="Yes"),
          Fact(Poor_impaired_Vision="Yes"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_19(self):
        self.declare(Fact(disease="Stroke"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="Yes"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="No"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="Yes"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="Yes"),
          Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_20(self):
        self.declare(Fact(disease="Tonsillitis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="Yes"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="No"),
          Fact(Headaches="No"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"), Fact(Nausea="No"),
          Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"), Fact(Poor_impaired_Vision="No"),
          Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="No"), Fact(Runny_Stuffy_nose="No"),
          Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"), Fact(Sneezing="No"), Fact(Sore_throat="No"),
          Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"), Fact(Swollen_lymphs="No"),
          Fact(Vaginal_Penile_discharge="Yes"), Fact(Vomiting="No"), Fact(Weight_Loss="No"), Fact(Yellowing="No"))
    def disease_21(self):
        self.declare(Fact(disease="Trichomoniasis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="Yes"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="Yes"), Fact(Cough_blood_Sputum="Yes"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="Yes"), Fact(Fever="Yes"),
          Fact(Headaches="No"), Fact(Loss_appetite="Yes"), Fact(Loss_Smell="No"), Fact(Malaise="Yes"),
          Fact(Nausea="No"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="Yes"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="Yes"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="Yes"),
          Fact(Yellowing="No"))
    def disease_22(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="Yes"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="Yes"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="Yes"), Fact(Loss_Smell="No"), Fact(Malaise="Yes"),
          Fact(Nausea="No"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="Yes"), Fact(Restlessness="Yes"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="No"), Fact(Weight_Loss="No"),
          Fact(Yellowing="No"))
    def disease_23(self):
        self.declare(Fact(disease="Typhoid"))

    @Rule(Fact(action='find_disease'), Fact(Bleeding="No"), Fact(Blindness="No"), Fact(Blisters_Lesions="No"),
          Fact(Bloating_Flatulence="No"), Fact(Discomfort_genitals="No"), Fact(Chills_Shivering="No"),
          Fact(Confusion_intellect_impairment="No"), Fact(Cough="No"), Fact(Cough_blood_Sputum="No"),
          Fact(Deafness="No"), Fact(Dehydration="No"), Fact(Fatigue_Tiredness="No"), Fact(Fever="Yes"),
          Fact(Headaches="Yes"), Fact(Loss_appetite="No"), Fact(Loss_Smell="No"), Fact(Malaise="No"),
          Fact(Nausea="Yes"), Fact(Numbness="No"), Fact(Pain="Yes"), Fact(Paralysis="No"),
          Fact(Poor_impaired_Vision="No"), Fact(Rash_Redness_Swelling_Itching="No"), Fact(Restlessness="No"),
          Fact(Runny_Stuffy_nose="No"), Fact(Seizures="No"), Fact(Shortness_Difficulty_breathing="No"),
          Fact(Sneezing="No"), Fact(Sore_throat="No"), Fact(Stiff_neck="No"), Fact(Stooling="No"), Fact(Sweating="No"),
          Fact(Swollen_lymphs="No"), Fact(Vaginal_Penile_discharge="No"), Fact(Vomiting="Yes"), Fact(Weight_Loss="No"),
          Fact(Yellowing="Yes"))
    def disease_24(self):
        self.declare(Fact(disease="Yellow_Fever"))

    @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("The most probable disease that you have is %s\n" % disease)

    @Rule(Fact(action='find_disease'), Fact(Bleeding=MATCH.Bleeding), Fact(Blindness=MATCH.Blindness),
          Fact(Blisters_Lesions=MATCH.Blisters_Lesions), Fact(Bloating_Flatulence=MATCH.Bloating_Flatulence),
          Fact(Discomfort_genitals=MATCH.Discomfort_genitals), Fact(Chills_Shivering=MATCH.Chills_Shivering),
          Fact(Confusion_intellect_impairment=MATCH.Confusion_intellect_impairment), Fact(Cough=MATCH.Cough),
          Fact(Cough_blood_Sputum=MATCH.Cough_blood_Sputum), Fact(Deafness=MATCH.Deafness),
          Fact(Dehydration=MATCH.Dehydration), Fact(Fatigue_Tiredness=MATCH.Fatigue_Tiredness), Fact(Fever=MATCH.Fever),
          Fact(Headaches=MATCH.Headaches), Fact(Loss_appetite=MATCH.Loss_appetite), Fact(Loss_Smell=MATCH.Loss_Smell),
          Fact(Malaise=MATCH.Malaise), Fact(Nausea=MATCH.Nausea), Fact(Numbness=MATCH.Numbness), Fact(Pain=MATCH.Pain),
          Fact(Paralysis=MATCH.Paralysis), Fact(Poor_impaired_Vision=MATCH.Poor_impaired_Vision),
          Fact(Rash_Redness_Swelling_Itching=MATCH.Rash_Redness_Swelling_Itching),
          Fact(Restlessness=MATCH.Restlessness), Fact(Runny_Stuffy_nose=MATCH.Runny_Stuffy_nose),
          Fact(Seizures=MATCH.Seizures), Fact(Shortness_Difficulty_breathing=MATCH.Shortness_Difficulty_breathing),
          Fact(Sneezing=MATCH.Sneezing), Fact(Sore_throat=MATCH.Sore_throat), Fact(Stiff_neck=MATCH.Stiff_neck),
          Fact(Stooling=MATCH.Stooling), Fact(Sweating=MATCH.Sweating), Fact(Swollen_lymphs=MATCH.Swollen_lymphs),
          Fact(Vaginal_Penile_discharge=MATCH.Vaginal_Penile_discharge), Fact(Vomiting=MATCH.Vomiting),
          Fact(Weight_Loss=MATCH.Weight_Loss), Fact(Yellowing=MATCH.Yellowing), NOT(Fact(disease=MATCH.disease)),
          salience=-999)
    def not_matched(self, Bleeding, Blindness, Blisters_Lesions, Bloating_Flatulence, Discomfort_genitals,
                    Chills_Shivering, Confusion_intellect_impairment, Cough, Cough_blood_Sputum, Deafness, Dehydration,
                    Fatigue_Tiredness, Fever, Headaches, Loss_appetite, Loss_Smell, Malaise, Nausea, Numbness, Pain,
                    Paralysis, Poor_impaired_Vision, Rash_Redness_Swelling_Itching, Restlessness, Runny_Stuffy_nose,
                    Seizures, Shortness_Difficulty_breathing, Sneezing, Sore_throat, Stiff_neck, Stooling, Sweating,
                    Swollen_lymphs, Vaginal_Penile_discharge, Vomiting, Weight_Loss, Yellowing):
        print("Did not find any disease that matches your exact symptoms\n")
        lis = [Bleeding, Blindness, Blisters_Lesions, Bloating_Flatulence, Discomfort_genitals, Chills_Shivering,
               Confusion_intellect_impairment, Cough, Cough_blood_Sputum, Deafness, Dehydration, Fatigue_Tiredness,
               Fever, Headaches, Loss_appetite, Loss_Smell, Malaise, Nausea, Numbness, Pain, Paralysis,
               Poor_impaired_Vision, Rash_Redness_Swelling_Itching, Restlessness, Runny_Stuffy_nose, Seizures,
               Shortness_Difficulty_breathing, Sneezing, Sore_throat, Stiff_neck, Stooling, Sweating, Swollen_lymphs,
               Vaginal_Penile_discharge, Vomiting, Weight_Loss, Yellowing]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and lis[j] == "Yes":
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)


preprocess()
engine = Greetings()
engine.reset()
prog_input = accept_input(
    ['No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No',
     'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No',
     'No', 'No', 'No'])
engine.run()
