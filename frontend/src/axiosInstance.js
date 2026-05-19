// import axios from 'axios'

// const baseURL = import.meta.env.VITE_BACKEND_BASE_URL

// const axiosInstance = axios.create({
//     baseURL: baseURL,
//     headers: {'Content-Type': 'application/json'}
// })

// // Request Interceptor
// axiosInstance.interceptors.request.use(
//     function(config) {
//         // Modify the request here
//         console.log("Config ->", config) // config is the request
//         const accessToken = localStorage.getItem("accessToken")
//         if (accessToken) {
//             config.headers['Authorization'] = `Bearer ${accessToken}`
//         }
//         return config
//     },
//     function (error) { // This function recieves an error object
//         return Promise.reject(error)
//     }
// )

// // Response Interceptor
// axiosInstance.interceptors.response.use(
//     function(response) {        
//         return response
//     },
//     async function(error) {
//         // Accept the original request -> Check for 401 error -> Call the token/refresh/ API -> get the new access token -> send the new access token with the request to /dashboard-protected
//         const originalRequest = error.config // Stores the original request using the config
//         if (error.response.status === 401 && !originalRequest.retry) {
//             originalRequest.retry = true
//             const refreshToken = localStorage.getItem("refreshToken")
//             try {
//                 const response = await axiosInstance.post('token/refresh/', {refresh: refreshToken}) // generating new access token
//                 console.log("Refresh token response: ", response.data)
//                 localStorage.setItem("accessToken", response.data.access)
//                 originalRequest.headers['Authorization'] = `Bearer ${response.data.access}`
//                 return axiosInstance(originalRequest) // send the updated request to the API
//             } catch(error) {
//                 // Handle Error
//                 localStorage.removeItem('accessToken') // Deletes Access token
//                 localStorage.removeItem('refreshToken') // Deletes Refresh token
//                 console.log(window.location.href) // should give /dashboard
//                 window.location.href = '/login'
//                 console.log(window.location.href) // should give /login
//             }
//         }
//     }
// )

// export default axiosInstance


import axios from 'axios'

const baseURL = import.meta.env.VITE_BACKEND_BASE_URL

const axiosInstance = axios.create({
    baseURL: baseURL,
    headers: {'Content-Type': 'application/json'},
    withCredentials: true
})

// Request Interceptor
axiosInstance.interceptors.request.use(
    function(config) {
        // Modify the request here
        console.log("Config ->", config) // config is the request
        return config
    },
    function (error) { // This function recieves an error object
        return Promise.reject(error)
    }
)

// Response Interceptor
axiosInstance.interceptors.response.use(
    function(response) {        
        return response
    },
    async function(error) {
        const originalRequest = error.config // Stores the original request using the config
        if (error.response.status === 401 && !originalRequest._retry 
            && !originalRequest.url.includes("refresh/") && !originalRequest.url.includes("dashboard-protected/")) {
            originalRequest._retry = true
            try {
                await axiosInstance.post('refresh/')
                return axiosInstance(originalRequest) // send the updated request to the API
            } catch(error) {
                // Handle Error
                window.location.href = '/login'
            }
        }
        return Promise.reject(error)
    }
)

export default axiosInstance