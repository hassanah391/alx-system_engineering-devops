# 🚨 Postmortem: The Great Downtime of 2025 🚨  

## Issue Summary  
**Duration:** February 26, 2025, 14:15 - 15:45 UTC (1 hour 30 minutes)  

**Impact:**  
- Our **GitHub Stats Web Service** became **unresponsive** due to excessive load on the caching layer.  
- **92% of API requests failed**, affecting developers tracking their GitHub contributions.  
- Some users reported **high latency** (>30 seconds) before timeouts.  

**Root Cause:**  
A sudden surge in API requests **overwhelmed Redis**, exhausting available memory and causing cache evictions, leading to **repeated expensive database lookups** (which we don’t have… because we don’t use a database).  


## 📜 Timeline  
- **14:15 UTC** – Monitoring alerted us to **API latency spikes** (we ignored it for a minute—big mistake).  
- **14:17 UTC** – Users on Twitter (X?) started posting “GitHub Stats is dead.” Panic ensued.  
- **14:20 UTC** – Engineers jumped into action. The **Redis instance was at 100% memory usage**.  
- **14:30 UTC** – Assumed it was a rogue process flooding Redis. Restarted the service. No improvement.  
- **14:50 UTC** – Noticed Redis logs showing **constant key evictions**—but why? 🤔  
- **15:10 UTC** – Found that a **sudden spike in API requests** caused massive cache churn, hammering the backend with redundant calculations.  
- **15:30 UTC** – Increased Redis memory, tweaked eviction policy, and restarted services.  
- **15:45 UTC** – Service restored. Users happy. Crisis averted.  


## 🧐 Root Cause & Resolution  

### **What Happened?**  
- The API saw **10x the usual traffic** due to a **viral tweet** about “cool GitHub stats.”  
- Redis, our only stateful component, **couldn’t hold the entire cache** and started evicting keys too quickly.  
- This caused **cache misses**, leading to repeated expensive computations that overloaded the system.  

### **How We Fixed It**  
- **Increased Redis memory** allocation (from 512MB to 2GB).  
- Switched the eviction policy to **LFU (Least Frequently Used)** to keep hot data longer.  
- Implemented **request rate limiting** to prevent API abuse.  


## 🔧 Corrective & Preventative Measures  

### **Lessons Learned:**  
1. **Monitor Redis memory usage proactively.** (Ignoring alerts = bad idea.)  
2. **Implement better caching strategies.** (Not all keys are equal.)  
3. **Prepare for sudden traffic spikes.** (Virality is a blessing and a curse.)  

### **🚀 Action Items:**  
✅ **Set Redis memory alerting at 80% usage.**  
✅ **Implement request rate limiting per user/IP.**  
✅ **Optimize cache storage strategy to keep only essential data.**  
✅ **Add a circuit breaker to prevent excessive backend requests during cache misses.**  


---

### **Final Thoughts**  
Sometimes, success comes at a price. This time, it was Redis’s soul. We live, we learn, and we add more monitoring. Onward! 🚀  
