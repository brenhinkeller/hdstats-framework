#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "integrator.h"

//Defining a new integrator object
//fxOld is a pointer to the previous period's x vector
struct integrator_t{
  int n;
  double dt;
  FuncPtr rhs;
  double *fxOld;
};

//Returning a new integrator object
Integrator *integrator_new(int n, double dt, FuncPtr rhs){
  Integrator *intNew = malloc(sizeof(Integrator));
  assert(intNew != NULL);
  intNew->n = n;
  intNew->dt = dt;
  intNew->rhs = rhs;
  intNew->fxOld = malloc(n*sizeof(double));
  assert(intNew->fxOld != NULL);
  return intNew;
 }

//Free the memory associated with the integrator
void integrator_free(Integrator *integrator){
  free(integrator->fxOld);
  free(integrator);
}

//Advance one timestep
int integrator_step(Integrator *integrator, double t, double *x){
  //Setting up local variables
  FuncPtr modelCalc = integrator->rhs;
  const int n = integrator->n;
  const double dt = integrator->dt;
  double fx[n];
  int i;

  //For the first time step, we do euler
  if(t==0){
  modelCalc(n,t,x,fx);
  x[0]=x[0]+dt*fx[0];
  integrator->fxOld[0]=fx[0];
  x[1]=x[1]+dt*fx[1];
  integrator->fxOld[1]=fx[1];
  }
  //For all other time steps, we do Adams-Bashford
  else{
    modelCalc(n,t,x,fx);
    for(i=0;i<n;i++){
      x[i]=x[i]+1.5*dt*fx[i]-.5*dt*integrator->fxOld[i];
      integrator->fxOld[i] = fx[i];
    }
  }
  return 0;
}