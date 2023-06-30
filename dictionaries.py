# data output path
data_out=('../')

# data input path
data_file = '/data/users/hgilmour/olr/olr_1h/1998/olr_merge_jul_1998.nc' #this is the 1 hourly mean olr data for Jul of 1998 (non-rainy season of el nino year)

# set up the parameters to convert from olr to tb
a = 1.228

# b
b = -1.106e-3

# stefan boltzmann constant
sigma = 5.67e-8 # W m^-2 K^-4

# path for the precipitation data
precip = '/data/users/hgilmour/total_precip/precip_instant/mi-ba751apq1998.nc' #this is the 1 hourly mean total precip data for all of 1998

# threshold values to be tested in sensitivity analysis
n_min_threshold_values = [118,987,1481,1550,1975,2469]

# set up the parameters for the dictionaries
position_threshold = 'weighted_diff'
sigma_threshold = 0.5
target = 'minimum'
threshold = 240
n_min_threshold = [118]
method = 'watershed'
v_max = 60
stubs = 7
order = 1
extrapolate = 0
memory = 0
adaptive_stop = 0.2
adaptive_step = 0.95
subnetwork_size = 15
method_linking = 'predict'
