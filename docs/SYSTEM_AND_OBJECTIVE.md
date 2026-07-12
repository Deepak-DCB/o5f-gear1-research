# System and objective

## System

The analyzed configuration is Lenovo Legion T7-34IMZ5 Type 90Q8, O5F Rocket
Lake BIOS, Intel Core i7-11700K, Lenovo Z490/Rocket Lake board, and 2 × 16 GB
DDR4-3200. Observed state is DDR4-3200 Gear 2.

Intel defines Gear 1 as controller/QCLK matching the DRAM clock and Gear 2 as a
half-rate controller relationship. Intel's public guidance identifies the
i9-11900K/KF as the 3200 Gear 1 exception among 11th-generation desktop SKUs;
that documented CPU behavior is not proof of identical O5F behavior on this
board. See [References](REFERENCES.md).

## Objective

Determine whether a normal, safe, recoverable O5F policy path can make the
target train and operate DDR4-3200 Gear 1. The final answer is no: the required
normal policy path, gate values, recovery, and verification route are not all
proven.

