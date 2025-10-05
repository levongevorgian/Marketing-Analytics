HW1 - Apple Vision Pro Diffusion Analysis

This repository contains my first homework for DS223 - Marketing Analytics. The assignment focuses on the diffusion of the Apple Vision Pro innovation, analyzed using the Bass Model and historical data from a look-alike product, Meta/Oculus Quest.

Directory Structure

img/

This directory contains all the images used in the project.
 • image1.png: Plot of historical shipment share of Meta/Oculus Quest headsets.
 • image2.png: Bass model fit to observed cumulative adoption.
 • image3.png: Predicted diffusion of Apple Vision Pro based on Bass Model.
 • image4.png: Estimated quarterly number of Apple Vision Pro adopters from 2023 to 2026, projected using the Bass Diffusion Model.
data/

This directory holds datasets used for analysis.
 • data.xlsx: Time series data of Meta/Oculus Quest shipments used to estimate Bass Model parameters.
report/

This directory contains the project report.
 • report.pdf: Final report in PDF format.
 • report_source.Rmd: Source R Markdown file used to generate the report.
README.md

The main documentation file. This file provides an overview of the project, instructions for setup, and usage.

Homework Overview

Every year, Time magazine publishes a list of the top 100 innovations. For this assignment:
 1 Choose an innovation from the list
2024 Innovations List
Apple Vision Pro product profile
 2 Identify a similar innovation from the past
Apple Vision Pro is compared to the Oculus Quest headset. Both devices offer immersive virtual/augmented reality experiences, with Apple Vision Pro extending the scope to work, media, and communication.
 3 Find historical data
Time series data on Meta/Oculus Quest headset shipments: Statista link
 4 Estimate Bass Model parameters
Using the historical data, the model estimates:
 ◦ p: Coefficient of innovation
 ◦ q: Coefficient of imitation
 ◦ M: Market potential
 5 Predict diffusion of the innovation
The Bass Model is used to project Apple Vision Pro adoption globally.
 6 Choose a scope
Global adoption is analyzed to capture worldwide market dynamics.
 7 Estimate the number of adopters by period
Predicted adoption per quarter is visualized and calculated using the Bass Model.

References

 • Statista — “AR/VR headset companies shipment share worldwide 2023–2025, by quarter.”
Click here for the link
