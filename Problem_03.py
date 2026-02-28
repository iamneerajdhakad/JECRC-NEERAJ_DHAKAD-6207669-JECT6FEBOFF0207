# Hospital Patient Visit Counter
class Solution:

    def department_patient_count(self, visits):
        dept_count = {}
        ## Write your code here & Don't forget to add return keyword
        for i in visits:
            department = i["department"]
            if department in dept_count:
                dept_count[department]+=1
            else:
                dept_count[department] = 1
            max_department = max(dept_count,key=dept_count.get)
        return dept_count,max_department