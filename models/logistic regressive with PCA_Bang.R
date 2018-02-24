data_train <- read.csv(file = "C:/Southampton/module two/Data mining/groupcoursework/traindata_Bang.csv", header=TRUE, sep = ",")
colnames(data_train)[1]<-c("Age")    #first block was garbled, changed to 'age'
str(data_train)                      #change the data type to string
org.fit<-glm(Attrition~.,data_train[,-c(8,18,23)],family=binomial(),control=list(maxit=100))         #glm function's default number of iterations is 25 times 
summary(org.fit)  
step(org.fit)

reducestepwise.fit <- glm(formula = Attrition ~ Age + BusinessTravel + Department + 
                            DistanceFromHome + EducationField + EnvironmentSatisfaction + 
                            Gender + JobInvolvement + JobLevel + JobSatisfaction + MaritalStatus + 
                            NumCompaniesWorked + OverTime + RelationshipSatisfaction + 
                            TotalWorkingYears + TrainingTimesLastYear + WorkLifeBalance + 
                            YearsAtCompany + YearsInCurrentRole + YearsSinceLastPromotion + 
                            YearsWithCurrManager, family = binomial(),data = data_train[,-c(8, 18, 23)], control = list(maxit = 100))
summary(reducestepwise.fit)  

#test <- predict(org.fit, newdata = data_train, type = "response")
test <- predict(reducestepwise.fit, newdata = data_train, type = "response")
test[test <0.5] <- 0  
test[test >= 0.5] <- 1 
result<-cbind(test,data_train$Attrition)  
table(test,data_train$Attrition) 

data_train[,2] <- as.factor(as.vector(data_train)[,2])     #change the Attrition to factor

library(caret)   # import package.  caret can do sampling analysis; add missing value; standardized data and do others data preprocessing.
library(ipred)

preprocess_data <- preProcess(data_train[,-c(2,8,18,23)],method=c("scale","center","pca"),na.remove=TRUE) 
#center means the Predicted value of the variable minus the mean
#scale means the Predicted value of the variable divided by standard deviation

fit.preprocess_data <- cbind(Attrition=data_train[,2],predict(preprocess_data,data_train[,-c(2,8,18,23)])) 
normalized.fit <- glm(Attrition~.,data = fit.preprocess_data,family=binomial())
summary(normalized.fit)  
step(normalized.fit)
fit.afterstep <- glm(formula = Attrition ~ BusinessTravel + EducationField + Gender + 
                       JobRole + MaritalStatus + OverTime + PC1 + PC4 + PC7 + PC8 + 
                       PC9 + PC13 + PC14 + PC15, family = binomial(), data = fit.preprocess_data)
summary(fit.afterstep )


test <- predict(fit.afterstep, newdata = fit.preprocess_data, type = "response")  
#test <- predict(fit.afterstep, newdata = data_train, type = "response")
test[test >= 0.55] <- 1
test[test < 0.55] <-0
result<-cbind(test,data_train$Attrition)  
table(test,data_train$Attrition) 

data_test <- read.csv("C:/Southampton/module two/Data mining/groupcoursework/testdata_Bang.csv", sep=",", header=TRUE)  
colnames(data_test)[1]<-c("Age")   

pre_data <- predict(preprocess_data ,data_test[,-c(2,8,18,23)])  
result1<- predict(fit.afterstep,pre_data ,interval = "prediction", level = 0.95)  
#result1 <- predict(normalized.fit,pre_data ,interval = "prediction", level = 0.95) 
 
result1[result1 >= 0.8] <- 1  #can change the degree 0.8
result1[result1 <0.8] <- 0  

table(result1,data_test$Attrition) 

