#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "integrator.h"

//Defining a new integrator object
struct integrator_t{
  int n;
  double dt;
  FuncPtr rhs;
};

//Returning a new integrator object
Integrator *integrator_new(int n, double dt, FuncPtr rhs){
  Integrator *intNew = malloc(sizeof(Integrator));
  assert(intNew != NULL);
  intNew->n = n;
  intNew->dt = dt;
  intNew->rhs = rhs;
  return intNew;
 }

//Free the memory associated with integrator
void integrator_free(Integrator *integrator){
free(integrator);
}

//Advance one timestep
int integrator_step(Integrator *integrator, double t, double *x){
  //Setting up local variables
  FuncPtr modelCalc = integrator->rhs;
  const double dt = integrator->dt;
  const int n = integrator->n;
  double fx[n];

  //Calling model specific function to calculate rhs
  modelCalc(n,t,x,fx);

  //Setting k1, and finding x values to plug into model Calc to find k2 of Runge-Kutta
  double k1[n];
  double newX[n];
  int i;
  for(i=0;i<n;i++){
    k1[i] = fx[i];
    newX[i] = x[i]+k1[i]*dt/2; 
  }
  modelCalc(n,t+dt/2,newX,fx);

  //Setting k2, and finding x values to plug into model calc to find k3 of Runge-Kutta
  double k2[n];
  for(i=0;i<n;i++){
    k2[i] = fx[i];
    newX[i] = x[i]+k2[i]*dt/2; 
  }
  modelCalc(n,t+dt/2,newX,fx);
  
  //Setting k3, and finding x for k4
  double k3[n];
  for(i=0;i<n;i++){
    k3[i] = fx[i];
    newX[i] = x[i]+dt*k3[i]; 
  }
  modelCalc(n,t+dt/2,newX,fx);
  
  //Setting k4, and finding actual x's using previous calculations
  double k4[n];
  for(i=0;i<n;i++){
    k4[i] = fx[i]; 
    x[i] = x[i]+dt*k1[i]/6+dt*(k2[i]+k3[i])/3+dt*k4[i]/6;
  }

  return 0;
}