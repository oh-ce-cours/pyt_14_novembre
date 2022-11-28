#ifdef _MSC_VER
#define EXPORT_SYMBOL __declspec(dllexport)
#else
#define EXPORT_SYMBOL
#endif

EXPORT_SYMBOL float cmult(int int_param, float float_param);
EXPORT_SYMBOL void square_numpy(float *in, float *out, int len);
EXPORT_SYMBOL float *demo_2d_array(int N, int M);