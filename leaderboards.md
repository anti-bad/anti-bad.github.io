---
layout: default
title: Leaderboards
permalink: /leaderboards/
---

The **Anti-Backdoor (Anti-BAD) Challenge** leaderboards display participants' final results across all tracks and tasks. Scores are percentages (geometric mean of utility and backdoor mitigation), where higher is better. For evaluation metrics and scoring details, see the [**Challenge**](/challenge/) page.

---

### Test Phase Results

*Results announced on February 18, 2026.*

Congratulations to all participants, and special thanks to everyone who contributed to making this challenge a success.

<div class="leaderboard-wrapper">
<table class="leaderboard-table">
<thead>
<tr>
  <th>Rank</th>
  <th>Team</th>
  <th>Overall</th>
  <th>Gen Task 1</th>
  <th>Gen Task 2</th>
  <th>Cls Task 1</th>
  <th>Cls Task 2</th>
  <th>Mul Task 1</th>
  <th>Mul Task 2</th>
</tr>
</thead>
<tbody>
<tr class="rank-gold">
  <td>🥇</td><td>AIST_ICT</td><td><strong>90.98</strong></td><td>90.86</td><td>92.43</td><td>95.49</td><td>95.83</td><td>95.08</td><td>76.21</td>
</tr>
<tr class="rank-silver">
  <td>🥈</td><td>UNIST</td><td><strong>87.07</strong></td><td>91.29</td><td>92.79</td><td>87.26</td><td>87.64</td><td>95.11</td><td>68.33</td>
</tr>
<tr class="rank-bronze">
  <td>🥉</td><td>ptrcklv</td><td><strong>86.76</strong></td><td>89.69</td><td>93.64</td><td>83.90</td><td>91.69</td><td>94.30</td><td>67.32</td>
</tr>
<tr>
  <td>4</td><td>ibaharul</td><td><strong>83.85</strong></td><td>89.71</td><td>92.92</td><td>79.49</td><td>76.10</td><td>93.59</td><td>71.29</td>
</tr>
<tr>
  <td>5</td><td>trkosire</td><td><strong>83.67</strong></td><td>90.59</td><td>93.42</td><td>77.92</td><td>75.02</td><td>93.75</td><td>71.29</td>
</tr>
<tr>
  <td>6</td><td>chrisbot77</td><td><strong>82.18</strong></td><td>91.13</td><td>92.80</td><td>76.14</td><td>75.20</td><td>94.95</td><td>62.87</td>
</tr>
<tr>
  <td>7</td><td>nidala</td><td><strong>81.00</strong></td><td>91.20</td><td>93.08</td><td>76.34</td><td>75.20</td><td>89.81</td><td>60.40</td>
</tr>
<tr>
  <td>8</td><td>DCL</td><td><strong>63.64</strong></td><td>91.21</td><td>89.11</td><td>76.54</td><td>54.62</td><td>22.54</td><td>47.85</td>
</tr>
<tr>
  <td>9</td><td>summu</td><td><strong>9.06</strong></td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>54.36</td>
</tr>
<tr class="reference-row">
  <td>—</td><td><em>Clean reference</em></td><td><em>87.45</em></td><td><em>87.29</em></td><td><em>89.44</em></td><td><em>88.15</em></td><td><em>91.86</em></td><td><em>96.82</em></td><td><em>71.14</em></td>
</tr>
<tr class="reference-row">
  <td>—</td><td><em>Baseline (WAG)</em></td><td><em>81.15</em></td><td><em>91.20</em></td><td><em>92.87</em></td><td><em>75.73</em></td><td><em>75.20</em></td><td><em>89.47</em></td><td><em>62.44</em></td>
</tr>
</tbody>
</table>
</div>

*Notably, the top-ranked submission achieved an overall score surpassing the clean reference.*

Two reference rows are included for context:
- **Clean reference** — for each task, a model trained on a clean dataset without any backdoor injection, reflecting the performance achievable under clean training conditions.
- **Baseline (WAG)** — the provided baseline method, which applies weighted averaging across the given backdoored models.

---

### Development Phase Results

*Final standings at the close of the development phase (November 7, 2025 – January 31, 2026).*

<div class="leaderboard-wrapper">
<table class="leaderboard-table">
<thead>
<tr>
  <th>Rank</th>
  <th>Team</th>
  <th>Overall</th>
  <th>Gen Task 1</th>
  <th>Gen Task 2</th>
  <th>Cls Task 1</th>
  <th>Cls Task 2</th>
  <th>Mul Task 1</th>
  <th>Mul Task 2</th>
</tr>
</thead>
<tbody>
<tr>
  <td>1</td><td>AIST_ICT</td><td><strong>93.10</strong></td><td>89.26</td><td>90.76</td><td>94.50</td><td>97.49</td><td>94.11</td><td>92.49</td>
</tr>
<tr>
  <td>2</td><td>UNIST (seungb)</td><td><strong>91.54</strong></td><td>86.07</td><td>91.84</td><td>90.61</td><td>94.16</td><td>94.39</td><td>92.16</td>
</tr>
<tr>
  <td>3</td><td>ptrcklv</td><td><strong>89.97</strong></td><td>84.15</td><td>87.67</td><td>91.29</td><td>92.99</td><td>92.55</td><td>91.15</td>
</tr>
<tr>
  <td>4</td><td>DCL (chrisbot77)</td><td><strong>87.70</strong></td><td>82.85</td><td>89.05</td><td>89.51</td><td>90.69</td><td>84.32</td><td>89.81</td>
</tr>
<tr>
  <td>5</td><td>nidala</td><td><strong>87.47</strong></td><td>82.02</td><td>89.15</td><td>89.51</td><td>88.80</td><td>85.68</td><td>89.66</td>
</tr>
<tr>
  <td>6</td><td>DCL (abdellahelmrini)</td><td><strong>87.16</strong></td><td>82.61</td><td>88.23</td><td>88.98</td><td>91.43</td><td>82.24</td><td>89.47</td>
</tr>
<tr>
  <td>7</td><td>299</td><td><strong>86.97</strong></td><td>83.01</td><td>88.96</td><td>86.17</td><td>89.19</td><td>84.85</td><td>89.64</td>
</tr>
<tr>
  <td>8</td><td>trkosire</td><td><strong>79.35</strong></td><td>81.98</td><td>87.31</td><td>89.33</td><td>89.91</td><td>41.07</td><td>86.50</td>
</tr>
<tr>
  <td>9</td><td>ibaharul</td><td><strong>79.09</strong></td><td>82.22</td><td>88.15</td><td>88.68</td><td>88.08</td><td>40.89</td><td>86.50</td>
</tr>
<tr>
  <td>10</td><td>gurubhandari</td><td><strong>77.40</strong></td><td>71.70</td><td>73.24</td><td>88.15</td><td>77.95</td><td>76.40</td><td>76.95</td>
</tr>
<tr>
  <td>11</td><td>UNIST (kiwan_kwon)</td><td><strong>63.74</strong></td><td>84.64</td><td>89.03</td><td>73.18</td><td>62.06</td><td>28.71</td><td>44.84</td>
</tr>
<tr>
  <td>12</td><td>Durinn AS</td><td><strong>54.69</strong></td><td>72.05</td><td>71.18</td><td>16.73</td><td>50.38</td><td>45.35</td><td>72.43</td>
</tr>
<tr>
  <td>13</td><td>Robin</td><td><strong>12.41</strong></td><td>0.00</td><td>0.00</td><td>74.44</td><td>0.00</td><td>0.00</td><td>0.00</td>
</tr>
<tr>
  <td>14</td><td>qafig</td><td><strong>12.16</strong></td><td>0.00</td><td>0.00</td><td>72.98</td><td>0.00</td><td>0.00</td><td>0.00</td>
</tr>
<tr class="reference-row">
  <td>—</td><td><em>Clean reference</em></td><td><em>90.51</em></td><td><em>84.49</em></td><td><em>86.33</em></td><td><em>90.39</em></td><td><em>95.66</em></td><td><em>94.87</em></td><td><em>91.32</em></td>
</tr>
<tr class="reference-row">
  <td>—</td><td><em>Baseline (WAG)</em></td><td><em>87.38</em></td><td><em>83.03</em></td><td><em>88.67</em></td><td><em>89.86</em></td><td><em>88.26</em></td><td><em>84.85</em></td><td><em>89.64</em></td>
</tr>
</tbody>
</table>
</div>

