#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "integrator.h" 

int duffing(int n, double t, const double *x, double *fx){
  const double gamma = .3;
  const double delta = .2;
  const double omega = 1;
  fx[1]=x[0];
  fx[0]=x[1]-pow(x[1],3)-delta*(x[0])+gamma*cos(omega*t);
  return 0;
}

int main(int argc, char *argv[]){
  //First we check to see if the current number of arguments was entered
  if (argc < 3){
    printf("Sorry, too few arguments. You must supply the timestep and number of steps to take."); 
    return 1; 
 }
  if (argc > 3) {
    printf("Sorry, too many arguments. You must supply the timestep and number of steps to take.");
    return 1;
  }

  //Setting arguments from command line
  const double timeStep = atof(argv[1]);
  const int nSteps = atoi(argv[2]);

  //initial values and printing
  const int n = 2;
  double t = 0;
  double x[2] = {0};


  //Creating Integrator
  FuncPtr duffingpt = &duffing;
  Integrator *eulerInt = integrator_new(n,timeStep,duffingpt);

  //Looping through the steps and printing output
  int i;
  for(i=0;i<(nSteps+1);i++){
    printf("%15.8f\t",t);
    printf("%15.8f\t",x[0]);
    printf("%15.8f\t",x[1]);
    printf("\n");

    integrator_step(eulerInt, t, x);
    t = t+timeStep;
  }

  //Free memory and exit
  integrator_free(eulerInt);
  return 0;
}

