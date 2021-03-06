/*****************************************************************************
 * Project: RooFit                                                           *
 *                                                                           *
  * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/

#ifndef ROOANAEXPNPDF
#define ROOANAEXPNPDF

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooCategoryProxy.h"
#include "RooAbsReal.h"
#include "RooAbsCategory.h"
 
class RooAnaExpNPdf : public RooAbsPdf {
public:
  RooAnaExpNPdf() {} ; 
  RooAnaExpNPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c,
	      RooAbsReal& _n);
  RooAnaExpNPdf(const RooAnaExpNPdf& other, const char* name=0) ;
  virtual TObject* clone(const char* newname) const { return new RooAnaExpNPdf(*this,newname); }
  inline virtual ~RooAnaExpNPdf() { }

  Int_t getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName=0) const ;
  Double_t analyticalIntegral(Int_t code, const char* rangeName=0) const ;

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy n ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAnaExpNPdf,1) // Your description goes here...
};
 
#endif
